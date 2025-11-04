# -*- coding: utf-8 -*-
"""
Portfolio Manager für AI-Powered Stock Investment Competition

Regeln:
- Starting Capital: €1,000
- 5-15 Positionen erforderlich (Diversifikation)
- Max 1 Trade pro Tag
- 3-Tage Mindesthaltedauer nach Kauf
- Keine Shorting, Options, Leverage
- Nur Long Positions (Stocks + ETFs)

Portfolio-Allokation (aus Investment Thesis):
- 50% USA (Tech/AI)
- 30% Hong Kong (Digital Platforms)
- 20% Japan (Automation/Innovation)
- Optional: 10% ETFs (Diversifikation)

Author: Investment Team
"""

import pandas as pd
import json
from datetime import datetime, timedelta
import pytz

# -----------------------------
# Configuration
# -----------------------------
STARTING_CAPITAL = 1000.0  # EUR
MIN_POSITIONS = 5
MAX_POSITIONS = 15
MAX_TRADES_PER_DAY = 1
MIN_HOLD_DAYS = 3

# Portfolio Allocation Targets (aus Investment Thesis)
TARGET_ALLOCATION = {
    "US": 0.50,  # 50% USA
    "HK": 0.30,  # 30% Hong Kong
    "JP": 0.20,  # 20% Japan
    "EU": 0.00,  # Optional: ETFs
}

# Risk Management
MAX_POSITION_SIZE = 0.25  # Max 25% in einer einzelnen Aktie
STOP_LOSS_THRESHOLD = -0.08  # -8% Stop-Loss Trigger (aus Thesis)
MAX_PORTFOLIO_DRAWDOWN = -0.10  # -10% maximaler Drawdown

# -----------------------------
# Portfolio Klasse
# -----------------------------
class Portfolio:
    def __init__(self, starting_capital=STARTING_CAPITAL):
        self.starting_capital = starting_capital
        self.cash = starting_capital
        self.positions = {}  # {ticker: {"shares": int, "avg_price": float, "buy_date": datetime}}
        self.trade_history = []
        self.daily_values = []
        
    def can_trade_today(self, target_date):
        """Prüft ob heute schon gehandelt wurde (Max 1 Trade pro Tag)"""
        trades_today = [t for t in self.trade_history 
                       if t["date"].date() == target_date.date()]
        return len(trades_today) < MAX_TRADES_PER_DAY
    
    def can_sell(self, ticker, target_date):
        """Prüft ob Mindesthaltedauer (3 Tage) erreicht ist"""
        if ticker not in self.positions:
            return False
        buy_date = self.positions[ticker]["buy_date"]
        days_held = (target_date - buy_date).days
        return days_held >= MIN_HOLD_DAYS
    
    def buy(self, ticker, shares, price_eur, date, reason="", ai_model=""):
        """Kaufe Aktien"""
        total_cost = shares * price_eur
        
        if total_cost > self.cash:
            return {
                "success": False,
                "message": f"Nicht genug Cash: €{self.cash:.2f} verfügbar, €{total_cost:.2f} benötigt"
            }
        
        # Position Size Check (gegen Starting Capital wenn Portfolio leer)
        portfolio_value = self.get_portfolio_value({})
        if portfolio_value < self.starting_capital:
            portfolio_value = self.starting_capital
        if total_cost / portfolio_value > MAX_POSITION_SIZE:
            return {
                "success": False,
                "message": f"Position zu groß: Max {MAX_POSITION_SIZE*100}% pro Aktie erlaubt"
            }
        
        # Ausführen
        self.cash -= total_cost
        
        if ticker in self.positions:
            # Durchschnittspreis berechnen
            old_shares = self.positions[ticker]["shares"]
            old_price = self.positions[ticker]["avg_price"]
            new_shares = old_shares + shares
            new_avg_price = (old_shares * old_price + shares * price_eur) / new_shares
            self.positions[ticker]["shares"] = new_shares
            self.positions[ticker]["avg_price"] = new_avg_price
        else:
            self.positions[ticker] = {
                "shares": shares,
                "avg_price": price_eur,
                "buy_date": date
            }
        
        # Trade loggen
        self.trade_history.append({
            "date": date,
            "action": "BUY",
            "ticker": ticker,
            "shares": shares,
            "price": price_eur,
            "total": total_cost,
            "cash_after": self.cash,
            "reason": reason,
            "ai_model": ai_model
        })
        
        return {
            "success": True,
            "message": f"Gekauft: {shares} x {ticker} @ €{price_eur:.2f} = €{total_cost:.2f}"
        }
    
    def sell(self, ticker, shares, price_eur, date, reason="", ai_model=""):
        """Verkaufe Aktien"""
        if ticker not in self.positions:
            return {
                "success": False,
                "message": f"{ticker} nicht im Portfolio"
            }
        
        if shares > self.positions[ticker]["shares"]:
            return {
                "success": False,
                "message": f"Nicht genug Aktien: {self.positions[ticker]['shares']} verfügbar"
            }
        
        # Mindesthaltedauer prüfen
        if not self.can_sell(ticker, date):
            buy_date = self.positions[ticker]["buy_date"]
            days_held = (date - buy_date).days
            return {
                "success": False,
                "message": f"Mindesthaltedauer nicht erreicht: {days_held} Tage (min {MIN_HOLD_DAYS})"
            }
        
        # Ausführen
        total_proceeds = shares * price_eur
        self.cash += total_proceeds
        
        # Position aktualisieren
        self.positions[ticker]["shares"] -= shares
        if self.positions[ticker]["shares"] == 0:
            del self.positions[ticker]
        
        # Trade loggen
        self.trade_history.append({
            "date": date,
            "action": "SELL",
            "ticker": ticker,
            "shares": shares,
            "price": price_eur,
            "total": total_proceeds,
            "cash_after": self.cash,
            "reason": reason,
            "ai_model": ai_model
        })
        
        return {
            "success": True,
            "message": f"Verkauft: {shares} x {ticker} @ €{price_eur:.2f} = €{total_proceeds:.2f}"
        }
    
    def get_portfolio_value(self, current_prices):
        """Berechne aktuellen Portfolio-Wert"""
        position_value = sum(
            self.positions[ticker]["shares"] * current_prices.get(ticker, self.positions[ticker]["avg_price"])
            for ticker in self.positions
        )
        return self.cash + position_value
    
    def get_position_summary(self, current_prices):
        """Aktuelle Positionen mit Gewinn/Verlust"""
        summary = []
        for ticker, pos in self.positions.items():
            current_price = current_prices.get(ticker, pos["avg_price"])
            current_value = pos["shares"] * current_price
            cost_basis = pos["shares"] * pos["avg_price"]
            pnl = current_value - cost_basis
            pnl_pct = (pnl / cost_basis) * 100 if cost_basis > 0 else 0
            
            # Handle timezone-aware datetime
            now = datetime.now(pytz.UTC)
            buy_date = pos["buy_date"]
            if buy_date.tzinfo is None:
                buy_date = pytz.UTC.localize(buy_date)
            
            summary.append({
                "ticker": ticker,
                "shares": pos["shares"],
                "avg_price": pos["avg_price"],
                "current_price": current_price,
                "cost_basis": cost_basis,
                "current_value": current_value,
                "pnl": pnl,
                "pnl_pct": pnl_pct,
                "days_held": (now - buy_date).days
            })
        
        return pd.DataFrame(summary)
    
    def check_stop_loss(self, current_prices):
        """Prüfe Stop-Loss Trigger (-8% aus Investment Thesis)"""
        alerts = []
        for ticker, pos in self.positions.items():
            current_price = current_prices.get(ticker, pos["avg_price"])
            loss_pct = (current_price - pos["avg_price"]) / pos["avg_price"]
            
            if loss_pct <= STOP_LOSS_THRESHOLD:
                alerts.append({
                    "ticker": ticker,
                    "loss_pct": loss_pct * 100,
                    "recommendation": f"STOP-LOSS TRIGGERED: {ticker} verloren {loss_pct*100:.1f}%"
                })
        
        return alerts
    
    def get_allocation(self, current_prices, ticker_regions):
        """Aktuelle Allokation nach Region"""
        allocation = {region: 0.0 for region in TARGET_ALLOCATION.keys()}
        total_value = self.get_portfolio_value(current_prices)
        
        for ticker, pos in self.positions.items():
            region = ticker_regions.get(ticker, "Unknown")
            current_price = current_prices.get(ticker, pos["avg_price"])
            position_value = pos["shares"] * current_price
            if region in allocation:
                allocation[region] += position_value
        
        # Als Prozent
        allocation_pct = {k: (v / total_value * 100) if total_value > 0 else 0 
                         for k, v in allocation.items()}
        
        return allocation_pct
    
    def export_to_csv(self, filename="portfolio_trades.csv"):
        """Exportiere Trade History als CSV für Competition Upload"""
        df = pd.DataFrame(self.trade_history)
        df.to_csv(filename, index=False)
        print(f"Trade History exportiert: {filename}")
        return df


# -----------------------------
# Trading Strategien
# -----------------------------
def analyze_buy_opportunities(prices_df, portfolio, max_positions=MAX_POSITIONS):
    """
    Analysiere Kaufgelegenheiten basierend auf:
    1. Portfolio hat noch Platz (< MAX_POSITIONS)
    2. Allokation entspricht Investment Thesis
    3. Genug Cash verfügbar
    """
    recommendations = []
    
    # Anzahl aktueller Positionen
    current_positions = len(portfolio.positions)
    
    if current_positions >= max_positions:
        return pd.DataFrame([{
            "message": f"Portfolio voll: {current_positions}/{max_positions} Positionen"
        }])
    
    # Verfügbares Cash
    available_cash = portfolio.cash
    
    # Finde Aktien die nicht im Portfolio sind
    for _, row in prices_df.iterrows():
        ticker = row["Ticker"]
        price_eur = row["Price EUR"]
        
        if pd.isna(price_eur):
            continue
        
        if ticker not in portfolio.positions:
            # Berechne mögliche Shares (max 25% des Portfolio-Werts)
            portfolio_value = portfolio.get_portfolio_value(
                {t: prices_df[prices_df["Ticker"]==t]["Price EUR"].values[0] 
                 for t in portfolio.positions}
            )
            max_investment = min(
                available_cash,
                portfolio_value * MAX_POSITION_SIZE
            )
            max_shares = int(max_investment / price_eur)
            
            if max_shares > 0:
                recommendations.append({
                    "ticker": ticker,
                    "name": row["Name"],
                    "sector": row["Sector"],
                    "region": row["Region"],
                    "price_eur": price_eur,
                    "max_shares": max_shares,
                    "max_investment": max_shares * price_eur,
                    "reason": "New position opportunity"
                })
    
    return pd.DataFrame(recommendations)


# -----------------------------
# Main Demo
# -----------------------------
def main():
    print("=" * 80)
    print("Portfolio Manager - AI Stock Investment Competition")
    print("=" * 80)
    
    # Lade aktuelle Preise
    try:
        prices_df = pd.read_csv("prices_2025-11-04_1615_Europe-Madrid.csv")
        print(f"\n✓ Preise geladen: {len(prices_df)} Aktien")
    except FileNotFoundError:
        print("\n✗ Keine Preise gefunden. Bitte zuerst price_getter ausführen!")
        return
    
    # Erstelle Portfolio
    portfolio = Portfolio(starting_capital=STARTING_CAPITAL)
    print(f"\n✓ Portfolio erstellt: €{portfolio.cash:.2f} Starting Capital")
    
    # Zeige verfügbare Aktien
    print("\n" + "=" * 80)
    print("VERFÜGBARE AKTIEN")
    print("=" * 80)
    print(prices_df[["Ticker", "Name", "Region", "Sector", "Price EUR"]].to_string(index=False))
    
    # Beispiel: Initial Trades gemäss Investment Thesis
    print("\n" + "=" * 80)
    print("BEISPIEL: INITIAL PORTFOLIO AUFBAU")
    print("=" * 80)
    
    target_date = datetime(2025, 11, 4, 16, 15)
    target_date = pytz.timezone("Europe/Madrid").localize(target_date)
    
    # US Positionen (50% Target = €500)
    initial_trades = [
        ("NVDA", 2, "Core AI hardware play"),
        ("AMD", 1, "Semiconductor/AI computing"),
        ("AMZN", 1, "Cloud & e-commerce leader"),
        # HK Positionen (30% Target = €300)
        ("0700.HK", 3, "Gaming & cloud leader Asia"),
        ("9988.HK", 8, "E-commerce & cloud China"),
        ("1810.HK", 15, "Consumer electronics growth"),
        # JP Positionen (20% Target = €200)
        ("9984.T", 1, "Tech investment exposure"),
        ("6758.T", 4, "Entertainment & tech diversification"),
        ("7203.T", 5, "Automotive EV leader"),
        # ETF für zusätzliche Diversifikation
        ("VWCE.DE", 1, "Global diversification ETF"),
    ]
    
    for ticker, shares, reason in initial_trades:
        if shares == 0:
            print(f"\n⊘ SKIP: {ticker} - {reason}")
            continue
            
        price_row = prices_df[prices_df["Ticker"] == ticker]
        if price_row.empty or pd.isna(price_row["Price EUR"].values[0]):
            print(f"\n✗ SKIP: {ticker} - Kein Preis verfügbar")
            continue
        
        price = price_row["Price EUR"].values[0]
        result = portfolio.buy(ticker, shares, price, target_date, reason, "Gemini Advanced")
        
        if result["success"]:
            print(f"\n✓ {result['message']}")
            print(f"  Reason: {reason}")
            print(f"  Cash remaining: €{portfolio.cash:.2f}")
        else:
            print(f"\n✗ {result['message']}")
    
    # Portfolio Summary
    print("\n" + "=" * 80)
    print("PORTFOLIO ÜBERSICHT")
    print("=" * 80)
    
    current_prices = {
        row["Ticker"]: row["Price EUR"] 
        for _, row in prices_df.iterrows() 
        if not pd.isna(row["Price EUR"])
    }
    
    total_value = portfolio.get_portfolio_value(current_prices)
    print(f"\nCash: €{portfolio.cash:.2f}")
    print(f"Positionen: {len(portfolio.positions)}/{MAX_POSITIONS}")
    print(f"Portfolio Wert: €{total_value:.2f}")
    print(f"Gewinn/Verlust: €{total_value - STARTING_CAPITAL:.2f} ({(total_value/STARTING_CAPITAL - 1)*100:.2f}%)")
    
    # Position Details
    if portfolio.positions:
        print("\n" + "-" * 80)
        positions_df = portfolio.get_position_summary(current_prices)
        print(positions_df.to_string(index=False))
    
    # Regional Allocation
    ticker_regions = {row["Ticker"]: row["Region"] for _, row in prices_df.iterrows()}
    allocation = portfolio.get_allocation(current_prices, ticker_regions)
    
    print("\n" + "-" * 80)
    print("REGIONAL ALLOCATION")
    print("-" * 80)
    for region, pct in allocation.items():
        target_pct = TARGET_ALLOCATION.get(region, 0) * 100
        diff = pct - target_pct
        status = "✓" if abs(diff) < 10 else "⚠"
        print(f"{status} {region:6s}: {pct:5.1f}% (Target: {target_pct:5.1f}%, Diff: {diff:+5.1f}%)")
    
    # Stop-Loss Check
    alerts = portfolio.check_stop_loss(current_prices)
    if alerts:
        print("\n" + "-" * 80)
        print("⚠ STOP-LOSS ALERTS")
        print("-" * 80)
        for alert in alerts:
            print(f"  {alert['recommendation']}")
    
    # Kaufgelegenheiten
    print("\n" + "=" * 80)
    print("WEITERE KAUFGELEGENHEITEN")
    print("=" * 80)
    opportunities = analyze_buy_opportunities(prices_df, portfolio)
    if not opportunities.empty and "ticker" in opportunities.columns:
        print(opportunities[["ticker", "name", "region", "price_eur", "max_shares", "max_investment"]].to_string(index=False))
    else:
        print(opportunities.to_string(index=False))
    
    # Export Trade History
    print("\n" + "=" * 80)
    trade_df = portfolio.export_to_csv("portfolio_trades.csv")
    print("\n✓ Competition Ready:")
    print("  - Trade Log: portfolio_trades.csv")
    print("  - Screenshot-Upload zu Teams: https://teams.microsoft.com")
    print("  - Max 1 Trade pro Tag, 3 Tage Mindesthaltedauer")
    

if __name__ == "__main__":
    main()

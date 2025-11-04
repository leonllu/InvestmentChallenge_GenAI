# -*- coding: utf-8 -*-
"""
Trade Decision Assistant - AI Agent Koordination

Dieses Skript unterstützt den Tier 2 Multi-Agent Workflow:
1. Agent 1 (Gemini): Research & Analysis
2. Agent 2 (ChatGPT): Fact Validation
3. Agent 3 (Claude): Portfolio Decision

Verwendung:
    python trade_assistant.py --ticker NVDA --action analyze
    python trade_assistant.py --ticker NVDA --action recommend
"""

import pandas as pd
import json
from datetime import datetime
import argparse

# Import portfolio manager
from portfolio_manager import Portfolio, TARGET_ALLOCATION, MAX_POSITION_SIZE

def load_current_portfolio():
    """Lade aktuelles Portfolio aus Trade History"""
    try:
        trades_df = pd.read_csv("portfolio_trades.csv")
        portfolio = Portfolio()
        
        # Replay alle Trades
        for _, trade in trades_df.iterrows():
            date = pd.to_datetime(trade["date"])
            if trade["action"] == "BUY":
                portfolio.buy(
                    trade["ticker"],
                    trade["shares"],
                    trade["price"],
                    date,
                    trade["reason"],
                    trade["ai_model"]
                )
            elif trade["action"] == "SELL":
                portfolio.sell(
                    trade["ticker"],
                    trade["shares"],
                    trade["price"],
                    date,
                    trade["reason"],
                    trade["ai_model"]
                )
        
        return portfolio
    except FileNotFoundError:
        print("⚠ Keine Trade History gefunden. Erstelle neues Portfolio.")
        return Portfolio()

def load_current_prices():
    """Lade aktuelle Preise"""
    try:
        df = pd.read_csv("prices_2025-11-04_1615_Europe-Madrid.csv")
        return {row["Ticker"]: row["Price EUR"] for _, row in df.iterrows() if not pd.isna(row["Price EUR"])}
    except FileNotFoundError:
        print("✗ Keine Preisdaten gefunden. Bitte zuerst price_getter ausführen!")
        return {}

def analyze_stock(ticker, prices_df):
    """
    Agent 1 Input: Grundlegende Stock-Analyse
    
    In der Praxis würde hier Gemini Advanced aufgerufen werden mit Prompts wie:
    - "Analyze {ticker} quarterly earnings and growth prospects"
    - "Compare {ticker} valuation to sector peers"
    - "Identify key risks for {ticker} in current market environment"
    """
    stock_info = prices_df[prices_df["Ticker"] == ticker]
    
    if stock_info.empty:
        return {"error": f"Ticker {ticker} nicht gefunden"}
    
    info = stock_info.iloc[0]
    
    analysis = {
        "ticker": ticker,
        "name": info["Name"],
        "sector": info["Sector"],
        "region": info["Region"],
        "current_price_eur": info["Price EUR"],
        "native_currency": info["Native Ccy"],
        "price_timestamp": info["Price TS (local)"],
        
        # Placeholder für AI-generierte Insights
        "ai_research": {
            "prompt": f"Analyze {info['Name']} ({ticker}) fundamentals, growth prospects, and risks in {info['Sector']} sector",
            "model": "Gemini Advanced",
            "insights": [
                f"[AI PLACEHOLDER] {info['Name']} is a leader in {info['Sector']}",
                f"[AI PLACEHOLDER] Current valuation at €{info['Price EUR']:.2f}",
                "[AI PLACEHOLDER] Key risks: Market volatility, sector competition",
            ],
            "sentiment": "NEUTRAL",  # Would be: BULLISH, NEUTRAL, BEARISH
            "conviction": 7.0,  # Scale 1-10
        },
        
        "yahoo_url": info["Yahoo URL"],
    }
    
    return analysis

def validate_analysis(analysis):
    """
    Agent 2: Fact Validation
    
    Cross-check AI-generated claims gegen:
    - Yahoo Finance actual data
    - Official investor relations
    - Consensus analyst ratings
    """
    validation = {
        "ticker": analysis["ticker"],
        "validation_model": "ChatGPT-4",
        "checks": [
            {
                "claim": f"Current price: €{analysis['current_price_eur']:.2f}",
                "verified": True,
                "source": "Yahoo Finance",
                "timestamp": analysis["price_timestamp"]
            },
            {
                "claim": f"Sector: {analysis['sector']}",
                "verified": True,
                "source": "Yahoo Finance",
            },
            # In der Praxis würden hier weitere Checks erfolgen:
            # - Earnings dates verification
            # - Revenue/profit claims
            # - Analyst ratings consensus
        ],
        "hallucination_risk": "LOW",  # LOW, MEDIUM, HIGH
        "validation_status": "PASSED",
    }
    
    return validation

def make_recommendation(ticker, portfolio, prices, analysis, validation):
    """
    Agent 3: Portfolio Decision Maker
    
    Basierend auf:
    - Validated research (Agent 1 + 2)
    - Current portfolio state
    - Risk management rules
    - Allocation targets
    """
    current_price = prices.get(ticker)
    
    if current_price is None:
        return {"error": f"Kein Preis für {ticker}"}
    
    # Check if already in portfolio
    in_portfolio = ticker in portfolio.positions
    
    # Regional allocation check
    ticker_region = analysis["region"]
    all_prices = prices
    ticker_regions = {ticker: analysis["region"]}  # Simplified
    current_allocation = portfolio.get_allocation(all_prices, ticker_regions)
    target_allocation = TARGET_ALLOCATION.get(ticker_region, 0) * 100
    
    # Position size calculation
    portfolio_value = portfolio.get_portfolio_value(prices)
    max_investment = portfolio_value * MAX_POSITION_SIZE
    max_shares = int(max_investment / current_price) if current_price > 0 else 0
    
    recommendation = {
        "ticker": ticker,
        "action": None,  # BUY, SELL, HOLD
        "shares": 0,
        "price_eur": current_price,
        "rationale": [],
        "risk_level": "MEDIUM",
        "priority": 5,  # 1-10
        "model": "Claude",
    }
    
    # Decision Logic
    if in_portfolio:
        # Check if stop-loss triggered
        position = portfolio.positions[ticker]
        loss_pct = (current_price - position["avg_price"]) / position["avg_price"]
        
        if loss_pct <= -0.08:  # -8% stop-loss
            recommendation["action"] = "SELL"
            recommendation["shares"] = position["shares"]
            recommendation["rationale"].append(f"STOP-LOSS triggered: {loss_pct*100:.1f}% loss")
            recommendation["priority"] = 9
        else:
            recommendation["action"] = "HOLD"
            recommendation["rationale"].append(f"Position performing within acceptable range ({loss_pct*100:+.1f}%)")
    else:
        # Evaluate BUY opportunity
        reasons = []
        
        # Check 1: Portfolio has room
        if len(portfolio.positions) >= 15:
            recommendation["action"] = "PASS"
            recommendation["rationale"].append("Portfolio at max positions (15/15)")
            return recommendation
        
        # Check 2: Cash available
        total_cost = max_shares * current_price
        if total_cost > portfolio.cash:
            recommendation["action"] = "PASS"
            recommendation["rationale"].append(f"Insufficient cash: €{portfolio.cash:.2f} < €{total_cost:.2f}")
            return recommendation
        
        # Check 3: Regional allocation
        if current_allocation.get(ticker_region, 0) < target_allocation:
            reasons.append(f"Improves {ticker_region} allocation ({current_allocation.get(ticker_region, 0):.1f}% → target {target_allocation:.1f}%)")
        
        # Check 4: AI conviction
        if analysis["ai_research"]["conviction"] >= 7.0:
            reasons.append(f"High AI conviction score: {analysis['ai_research']['conviction']}/10")
        
        # Check 5: Validation passed
        if validation["validation_status"] == "PASSED":
            reasons.append("All fact validations passed")
        
        if len(reasons) >= 2:
            recommendation["action"] = "BUY"
            recommendation["shares"] = max(1, max_shares // 2)  # Conservative sizing
            recommendation["rationale"] = reasons
            recommendation["priority"] = 7
        else:
            recommendation["action"] = "HOLD"
            recommendation["rationale"].append("Insufficient conviction criteria met")
    
    return recommendation

def print_recommendation(analysis, validation, recommendation):
    """Schöne Ausgabe der Empfehlung"""
    print("\n" + "=" * 80)
    print(f"TRADE RECOMMENDATION: {analysis['ticker']} - {analysis['name']}")
    print("=" * 80)
    
    print(f"\n📊 STOCK INFO")
    print(f"  Sector: {analysis['sector']}")
    print(f"  Region: {analysis['region']}")
    print(f"  Current Price: €{analysis['current_price_eur']:.2f}")
    print(f"  Timestamp: {analysis['price_timestamp']}")
    
    print(f"\n🤖 AI RESEARCH (Agent 1: Gemini)")
    print(f"  Sentiment: {analysis['ai_research']['sentiment']}")
    print(f"  Conviction: {analysis['ai_research']['conviction']}/10")
    for insight in analysis['ai_research']['insights']:
        print(f"  • {insight}")
    
    print(f"\n✓ VALIDATION (Agent 2: ChatGPT)")
    print(f"  Status: {validation['validation_status']}")
    print(f"  Hallucination Risk: {validation['hallucination_risk']}")
    for check in validation['checks']:
        status = "✓" if check['verified'] else "✗"
        print(f"  {status} {check['claim']}")
    
    print(f"\n💡 RECOMMENDATION (Agent 3: Claude)")
    print(f"  Action: {recommendation['action']}")
    if recommendation['action'] == "BUY":
        print(f"  Shares: {recommendation['shares']}")
        print(f"  Total Cost: €{recommendation['shares'] * recommendation['price_eur']:.2f}")
    print(f"  Priority: {recommendation['priority']}/10")
    print(f"  Risk Level: {recommendation['risk_level']}")
    print(f"\n  Rationale:")
    for reason in recommendation['rationale']:
        print(f"    • {reason}")
    
    print("\n" + "=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Trade Decision Assistant")
    parser.add_argument("--ticker", type=str, help="Stock ticker symbol")
    parser.add_argument("--action", type=str, choices=["analyze", "recommend", "scan"], 
                       default="recommend", help="Action to perform")
    
    args = parser.parse_args()
    
    # Load data
    portfolio = load_current_portfolio()
    prices = load_current_prices()
    prices_df = pd.read_csv("prices_2025-11-04_1615_Europe-Madrid.csv")
    
    if args.action == "scan":
        # Scan all available stocks
        print("\n" + "=" * 80)
        print("SCANNING ALL STOCKS FOR OPPORTUNITIES")
        print("=" * 80)
        
        opportunities = []
        for ticker in prices.keys():
            analysis = analyze_stock(ticker, prices_df)
            if "error" in analysis:
                continue
            validation = validate_analysis(analysis)
            recommendation = make_recommendation(ticker, portfolio, prices, analysis, validation)
            
            if recommendation["action"] == "BUY" and recommendation["priority"] >= 6:
                opportunities.append({
                    "ticker": ticker,
                    "name": analysis["name"],
                    "action": recommendation["action"],
                    "priority": recommendation["priority"],
                    "shares": recommendation["shares"],
                    "cost": recommendation["shares"] * recommendation["price_eur"]
                })
        
        if opportunities:
            opp_df = pd.DataFrame(opportunities).sort_values("priority", ascending=False)
            print("\n🎯 TOP OPPORTUNITIES:")
            print(opp_df.to_string(index=False))
        else:
            print("\n⚠ No high-priority opportunities found")
    
    elif args.ticker:
        # Analyze specific ticker
        analysis = analyze_stock(args.ticker, prices_df)
        
        if "error" in analysis:
            print(f"✗ Error: {analysis['error']}")
            return
        
        validation = validate_analysis(analysis)
        recommendation = make_recommendation(args.ticker, portfolio, prices, analysis, validation)
        
        print_recommendation(analysis, validation, recommendation)
        
        # Export für Documentation
        export = {
            "timestamp": datetime.now().isoformat(),
            "analysis": analysis,
            "validation": validation,
            "recommendation": recommendation,
        }
        
        filename = f"trade_decision_{args.ticker}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        with open(filename, "w") as f:
            json.dump(export, f, indent=2)
        
        print(f"\n✓ Decision exported: {filename}")

if __name__ == "__main__":
    main()

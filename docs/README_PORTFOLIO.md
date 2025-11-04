# AI-Powered Stock Investment Competition - Portfolio Manager

## Übersicht

Dieses Repository enthält die Tools für die AI Stock Investment Competition (24. Okt - 14. Nov 2025).

**Starting Capital:** €1,000 (imaginary)  
**Investment Strategy:** Tech/AI fokussiert mit globaler Diversifikation  
**AI Tier:** Tier 2 (Coordinated Agents)

## 📁 Dateien

### 1. `price_getter` - Preisdaten Sammler
Holt aktuelle Börsenkurse von Yahoo Finance und konvertiert sie nach EUR.

**Features:**
- Unterstützt 17 Aktien aus 4 Regionen (US, Hong Kong, Japan, EU)
- Automatischer Fallback auf Tagesschlusskurse bei geschlossenen Märkten
- FX-Konvertierung (USD, HKD, JPY → EUR)
- CSV Export für weitere Analyse

**Verwendung:**
```bash
python price_getter
```

**Output:** `prices_2025-11-04_1615_Europe-Madrid.csv`

### 2. `portfolio_manager.py` - Portfolio Management System
Verwaltet Trades und analysiert Portfolio nach Competition-Regeln.

**Features:**
- ✓ Regelkonformität: Max 1 Trade/Tag, 3-Tage Mindesthaltedauer
- ✓ Position Sizing: Max 25% pro Aktie
- ✓ Stop-Loss Monitoring: -8% Trigger (aus Investment Thesis)
- ✓ Regional Allocation Tracking: US 50%, HK 30%, JP 20%
- ✓ Trade History Export (CSV für Competition Upload)

**Verwendung:**
```bash
python portfolio_manager.py
```

**Output:** `portfolio_trades.csv`

## 📊 Aktuelles Portfolio

### Positionen (6/15)

| Ticker | Name | Shares | Price EUR | Value EUR | Region | Sector |
|--------|------|--------|-----------|-----------|--------|--------|
| AMD | AMD | 1 | 222.48 | 222.48 | US | Semiconductors |
| AMZN | Amazon | 1 | 221.32 | 221.32 | US | Cloud/E-commerce |
| 0700.HK | Tencent | 3 | 70.49 | 211.48 | HK | Gaming/Cloud |
| 9988.HK | Alibaba | 8 | 17.82 | 142.56 | HK | E-commerce/Cloud |
| 1810.HK | Xiaomi | 15 | 4.87 | 72.99 | HK | Consumer Tech |
| 6758.T | Sony | 4 | 24.38 | 97.52 | JP | Entertainment/Tech |

**Total Portfolio Value:** €1,000.00  
**Cash Remaining:** €31.65  
**P&L:** €0.00 (0.00%)

### Regional Allocation

| Region | Actual | Target | Diff |
|--------|--------|--------|------|
| US | 44.4% | 50.0% | -5.6% ✓ |
| HK | 42.7% | 30.0% | +12.7% ⚠ |
| JP | 9.8% | 20.0% | -10.2% ⚠ |
| EU | 0.0% | 0.0% | +0.0% ✓ |

**Anmerkung:** Hong Kong ist leicht übergewichtet, Japan untergewichtet. Nächste Trades sollten JP-Positionen aufbauen.

## 🎯 Investment Thesis (Kurzfassung)

**Strategie:** Aggressive Growth in Tech/AI  
**Zeithorizont:** 3 Wochen (Simulation)  
**Target Return:** 8-15%  
**Max Drawdown:** -10%

### Portfolio Allokation
- **50% USA:** NVIDIA, AMD, Amazon, Microsoft, Google, Meta, Tesla
- **30% Hong Kong:** Tencent, Alibaba, Xiaomi, Meituan
- **20% Japan:** SoftBank, Keyence, Sony, Toyota
- **Optional:** ETFs (VWCE, EQQQ) für zusätzliche Diversifikation

### Sektoren
1. **AI/Semiconductors:** NVIDIA, AMD (Core Holdings)
2. **Cloud Computing:** Microsoft, Amazon, Alibaba
3. **Digital Platforms:** Tencent, Meta, Google
4. **Automation:** Keyence, Sony, Toyota
5. **EV/Autonomous:** Tesla

## 📋 Competition Regeln

### Trading Restrictions
- ✗ Kein Shorting (nur Long-Positionen)
- ✗ Keine Options/Derivatives
- ✗ Kein Leverage (1:1 Cash only)
- ✓ Nur Stocks + ETFs
- ✓ Max 1 Trade pro Tag
- ✓ Min 3 Tage Haltedauer nach Kauf
- ✓ 5-15 Positionen erforderlich

### Dokumentationspflicht
**Jeder Trade muss dokumentiert werden:**
1. Screenshot von Yahoo Finance (Preis, Datum, Zeit)
2. Upload zu Microsoft Teams innerhalb 5 Minuten
3. Teams Timestamp = offizieller Trade-Zeitpunkt
4. Link in Trade Log eintragen

## 🤖 AI Architecture (Tier 2)

### Agent 1: Market Research Analyst (Gemini Advanced)
**Rolle:** Fundamentalanalyse und Markttrends  
**Input:** Company reports, earnings, news  
**Output:** Research insights + sentiment score

### Agent 2: Fact Validator (ChatGPT-4)
**Rolle:** Verifizierung von Daten  
**Input:** Agent 1 claims  
**Output:** Verified facts vs. Yahoo Finance

### Agent 3: Portfolio Decision Maker (Claude)
**Rolle:** Trade-Empfehlungen  
**Input:** Validated research + current portfolio  
**Output:** BUY/SELL recommendations mit Rationale

### Workflow
```
Research → Validation → Decision → Human Approval → Trade Execution → Documentation
```

## 🎲 Nächste Schritte

### Kaufgelegenheiten (basierend auf aktuellem Portfolio)
1. **Erhöhe JP Allocation:**
   - Toyota (7203.T): €17.91 → 1 Share = €17.91
   - Oder mehr SoftBank wenn Cash verfügbar

2. **Reduziere HK Übergewichtung:**
   - Ggf. teilweise Verkauf nach 3-Tage Mindesthaltedauer (7. Nov)

3. **Erwäge US-Erweiterung:**
   - NVIDIA: Weitere Shares bei Pullback
   - Microsoft: Core AI/Cloud Position noch fehlt

### Trade Timing (3-Tage Hold beachten!)
- **Heute (4. Nov):** Initial Trades ausgeführt
- **Früheste Verkäufe:** 7. November 2025
- **Verbleibende Trades:** 7-9 weitere Positionen möglich

## 📊 Risk Management

### Stop-Loss Policy
- **Trigger:** -8% auf einzelne Position
- **Action:** Review & ggf. Position reduzieren
- **Monitoring:** Täglich via `portfolio_manager.py`

### Diversifikation
- **Min Positionen:** 5 (erreicht ✓)
- **Max Positionen:** 15 (noch 9 verfügbar)
- **Max Position Size:** 25% pro Aktie

### Drawdown Management
- **Max Portfolio Drawdown:** -10%
- **Current Drawdown:** 0% (Day 1)

## 📝 Deliverables Timeline

| Datum | Deliverable | Status |
|-------|-------------|--------|
| 29. Okt | Investment Thesis (4 pages) | ✓ Submitted |
| 4. Nov | Initial Trades | ✓ Completed |
| 4. Nov | Mid-Competition Update (2 pages) | 🔄 Due Today |
| 12. Nov | Final Presentation | ⏳ Pending |
| 14. Nov | Awards Ceremony | 🎯 Goal |

## 🛠️ Installation

```bash
# Python Environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Dependencies
pip install pandas yfinance pytz PyPDF2

# Run Tools
python price_getter           # Holt aktuelle Preise
python portfolio_manager.py   # Analysiert Portfolio
```

## 📚 Referenzen

- **Yahoo Finance:** https://finance.yahoo.com/
- **Competition Guide:** `AI-Powered_Global_Stock_Investment_Competition.pdf`
- **Investment Thesis:** `deliverable1_investment_thesis.pdf`
- **Trade Log:** `portfolio_trades.csv`
- **Price Data:** `prices_2025-11-04_1615_Europe-Madrid.csv`

## ⚠️ Disclaimer

**Dies ist ein Bildungsprojekt mit imaginärem Kapital (€1,000).**

- ✗ NICHT mit echtem Geld handeln basierend auf LLM-Outputs
- ✗ LLMs halluzinieren regelmäßig Finanzdaten
- ✗ Keine Investment-Beratung
- ✓ Ziel: AI Validation Skills trainieren

---

**Team:** Investment Challenge GenAI  
**Competition Period:** 24. Okt - 14. Nov 2025  
**Target Return:** 8-15% (3 weeks)  
**AI Tier:** Tier 2 (Coordinated Agents)

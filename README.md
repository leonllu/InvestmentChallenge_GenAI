# AI-Powered Stock Investment Competition# InvestmentChallenge_GenAI

Automated trading system for the AI Stock Investment Competition (Oct 24 - Nov 14, 2025).

**Starting Capital:** €1,000 (imaginary)  
**Strategy:** Tech/AI focused with global diversification  
**AI Tier:** Tier 2 (Coordinated Agents)

---

## 📁 Ordnerstruktur

```
InvestmentChallenge_GenAI/
│
├── docs/                           # Dokumentation & Deliverables
│   ├── deliverables/              # Competition Submissions
│   │   ├── deliverable1_investment_thesis.pdf
│   │   └── deliverable2_mid_competition_update.pdf
│   ├── reference/                 # Reference Materials
│   │   └── AI-Powered_Global_Stock_Investment_Competition.pdf
│   ├── QUICK_REFERENCE.md         # Command Cheatsheet
│   └── README_PORTFOLIO.md        # Detailed Portfolio Documentation
│
├── tools/                          # Python Scripts & Tools
│   ├── price_getter               # Fetch stock prices from Yahoo Finance
│   ├── portfolio_manager.py       # Portfolio management & risk monitoring
│   ├── trade_assistant.py         # AI multi-agent decision workflow
│   └── generate_mid_competition_update.py  # PDF generator for reports
│
├── data/                           # Trading Data & Prices
│   ├── portfolio_trades.csv       # Trade log (competition official record)
│   └── prices_2025-11-04_1615_Europe-Madrid.csv  # Latest price snapshot
│
├── logs/                           # AI Decision Logs
│   └── trade_decision_*.json      # AI agent decision records
│
└── README.md                       # This file (Main documentation)
```

---

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Activate Python virtual environment
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies (if not already done)
pip install pandas yfinance pytz PyPDF2 reportlab
```

### 2. Daily Workflow

```bash
# Morning: Update prices
python tools/price_getter

# Analyze portfolio
python tools/portfolio_manager.py

# Scan for opportunities
python tools/trade_assistant.py --action scan

# Analyze specific stock
python tools/trade_assistant.py --ticker MSFT --action recommend
```

### 3. Generate Reports

```bash
# Mid-competition update (already done)
python tools/generate_mid_competition_update.py
```

---

## 📊 Current Portfolio Status

**Last Updated:** November 4, 2025, 16:15 CET

| Metric | Value |
|--------|-------|
| Starting Capital | €1,000.00 |
| Current Value | €1,000.00 |
| Cash Remaining | €31.65 |
| P&L | €0.00 (0.00%) |
| Positions | 6 / 15 |

### Holdings

| Ticker | Name | Region | Shares | Value | Allocation |
|--------|------|--------|--------|-------|------------|
| AMD | AMD | US | 1 | €222.48 | 22.2% |
| AMZN | Amazon | US | 1 | €221.32 | 22.1% |
| 0700.HK | Tencent | HK | 3 | €211.48 | 21.1% |
| 9988.HK | Alibaba | HK | 8 | €142.56 | 14.3% |
| 1810.HK | Xiaomi | HK | 15 | €72.99 | 7.3% |
| 6758.T | Sony | JP | 4 | €97.52 | 9.8% |

### Regional Allocation

| Region | Current | Target | Status |
|--------|---------|--------|--------|
| US | 44.4% | 50.0% | ✓ Close to target |
| Hong Kong | 42.7% | 30.0% | ⚠ Overweight |
| Japan | 9.8% | 20.0% | ⚠ Underweight |
| EU | 0.0% | 0.0% | ✓ As planned |

---

## 🤖 AI Architecture (Tier 2)

### Multi-Agent System

```
┌─────────────────────────────────────────────────────────┐
│  Agent 1: Market Research (Gemini Advanced)             │
│  → Fundamentalanalyse, Trends, Growth Prospects         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Agent 2: Fact Validator (ChatGPT-4)                    │
│  → Cross-check vs. Yahoo Finance, Filter Hallucinations │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Agent 3: Portfolio Decision Maker (Claude)             │
│  → BUY/SELL/HOLD Recommendations with Rationale         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Human Override & Trade Execution                       │
│  → Final approval, Screenshot to Teams, Log to CSV      │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Competition Rules

- ✓ **Max 1 Trade per Day**
- ✓ **3-Day Minimum Hold Period**
- ✓ **Position Size Limit:** Max 25% per stock
- ✓ **Portfolio Size:** 5-15 positions required
- ✓ **Long Only:** No shorting, options, or leverage
- ⚠ **Screenshot Requirement:** Upload to Teams within 5 minutes

---

## 📅 Timeline & Deliverables

| Date | Deliverable | Status |
|------|-------------|--------|
| Oct 29 | Investment Thesis (4 pages) | ✓ Submitted |
| Nov 4 | Mid-Competition Update (2 pages) | ✓ Submitted |
| Nov 12 | Final Presentation | ⏳ Pending |
| Nov 14 | Awards Ceremony | 🎯 Goal |

---

## 📈 Available Stocks (17 Total)

### United States (7 stocks)
- **AMD** - Semiconductors | €222.48
- **AMZN** - Cloud/E-commerce | €221.32
- **GOOGL** - AI/Search | €244.07
- **META** - Social Media/AI | €555.40
- **MSFT** - Cloud/AI | €446.74
- **NVDA** - AI Hardware | €176.27
- **TSLA** - EV/Autonomous | €400.56

### Hong Kong (4 stocks)
- **0700.HK** - Tencent - Gaming/Cloud | €70.49
- **1810.HK** - Xiaomi - Consumer Tech | €4.87
- **3690.HK** - Meituan - E-commerce/Delivery | €11.20
- **9988.HK** - Alibaba - E-commerce/Cloud | €17.82

### Japan (4 stocks)
- **6758.T** - Sony - Entertainment/Tech | €24.38
- **6861.T** - Keyence - Automation/Robotics | €320.81
- **7203.T** - Toyota - Automotive/EV | €17.91
- **9984.T** - SoftBank - Tech Investment | €142.81

### EU ETFs (2 stocks)
- **EQQQ.DE** - Invesco EQQQ Nasdaq-100 | €548.00
- **VWCE.DE** - Vanguard FTSE All-World | €145.54

---

## 🎯 Next Steps

### Immediate (Nov 5-7)
- [ ] Add Microsoft (MSFT) or Meta (META) → strengthen US allocation
- [ ] Add SoftBank (9984.T) or Toyota (7203.T) → strengthen JP allocation
- [ ] Expand to 10-12 positions for better diversification
- [ ] Daily monitoring: Stop-loss check (-8% trigger)

### Week 2 (Nov 7-11)
- [ ] Rebalance regional allocation: HK 42.7% → 30%, JP 9.8% → 20%
- [ ] Reduce tech concentration (currently 85%)
- [ ] Prepare final presentation materials

### Final Week (Nov 12-14)
- [ ] Submit final presentation (Nov 12)
- [ ] Awards ceremony (Nov 14)

---

## 🛡️ Risk Management

| Parameter | Target | Current |
|-----------|--------|---------|
| Min Positions | 5 | 6 ✓ |
| Max Positions | 15 | 6 ✓ |
| Max Position Size | 25% | 22.2% ✓ |
| Stop-Loss Trigger | -8% | N/A (Day 1) |
| Max Drawdown | -10% | 0% ✓ |
| Target Return | 8-15% | 0% (Day 1) |

---

## 🔗 Important Links

- **Yahoo Finance:** https://finance.yahoo.com/
- **Teams Channel:** #stock-competition-trades (screenshot upload)
- **Documentation:** See `docs/` folder
- **Quick Reference:** `docs/QUICK_REFERENCE.md`
- **Detailed Guide:** `docs/README_PORTFOLIO.md`

---

## ⚠️ Disclaimer

**This is an educational project with imaginary capital (€1,000).**

- ✗ Do NOT trade real money based on LLM outputs
- ✗ LLMs regularly hallucinate financial data
- ✗ This is NOT investment advice
- ✓ Goal: Learn AI validation skills in high-stakes domains

---

## 👥 Team

**Competition:** AI-Powered Stock Investment Competition  
**Period:** October 24 - November 14, 2025  
**Target Return:** 8-15% (3 weeks)  
**AI Tier:** Tier 2 (Coordinated Agents) → +10 bonus points

---

**Last Updated:** November 4, 2025  
**Status:** Day 1 - Portfolio Initialized ✓

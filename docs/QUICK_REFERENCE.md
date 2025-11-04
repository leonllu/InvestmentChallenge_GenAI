# QUICK REFERENCE - Investment Competition

## 📄 Deliverable 2 - FERTIG! ✓

**File:** `deliverable2_mid_competition_update.pdf` (11 KB)  
**Status:** ✓ Bereit zum Upload  
**Due:** November 4, 2025, 9:00 AM  

### Inhalt (2 Seiten):
1. **Performance Review** (0.5 Seiten)
   - Current Value: €1,000.00
   - P&L: €0.00 (0.00%)
   - 6 Positionen mit Tabellen
   - Regional Allocation Analysis

2. **AI System Learnings** (1 Seite)
   - Multi-Agent Architecture Details
   - Key Discoveries & Surprises
   - Validation Gaps Found
   - System Adjustments Made

3. **Revised Strategy** (0.5 Seiten)
   - Immediate Priorities (Nov 5-7)
   - Risk Mitigation Adjustments
   - AI Workflow Refinements
   - Target Outcomes

---

## 🗂️ Alle Competition Dateien

### Deliverables
- ✓ `deliverable1_investment_thesis.pdf` (3.5 KB) - Submitted 29. Okt
- ✓ `deliverable2_mid_competition_update.pdf` (11 KB) - DUE TODAY
- ⏳ Deliverable 3: Final Presentation - Due 12. Nov

### Trading Tools
- `price_getter` - Holt Preise von Yahoo Finance (17 Aktien)
- `portfolio_manager.py` - Portfolio Management & Risk Monitoring
- `trade_assistant.py` - AI Multi-Agent Workflow
- `generate_mid_competition_update.py` - PDF Generator

### Data Files
- `portfolio_trades.csv` - Trade Log (6 Trades)
- `prices_2025-11-04_1615_Europe-Madrid.csv` - Aktuelle Preise
- `trade_decision_*.json` - AI Decision Records

### Documentation
- `README_PORTFOLIO.md` - Vollständige System-Dokumentation
- `AI-Powered_Global_Stock_Investment_Competition.pdf` - Competition Guide

---

## 📊 Current Portfolio Status

**Starting Capital:** €1,000.00  
**Current Value:** €1,000.00  
**Cash:** €31.65  
**P&L:** €0.00 (0.00%)

### Holdings (6/15 Positions)
| Ticker | Name | Shares | Value | Region |
|--------|------|--------|-------|--------|
| AMD | AMD | 1 | €222.48 | US |
| AMZN | Amazon | 1 | €221.32 | US |
| 0700.HK | Tencent | 3 | €211.48 | HK |
| 9988.HK | Alibaba | 8 | €142.56 | HK |
| 1810.HK | Xiaomi | 15 | €72.99 | HK |
| 6758.T | Sony | 4 | €97.52 | JP |

### Regional Allocation
- **US:** 44.4% (Target: 50.0%) ✓ Close
- **HK:** 42.7% (Target: 30.0%) ⚠ Overweight
- **JP:** 9.8% (Target: 20.0%) ⚠ Underweight
- **EU:** 0.0% (Target: 0.0%) ✓

---

## 🎯 Nächste Schritte

### HEUTE (4. Nov)
- [x] Mid-Competition Update erstellt
- [ ] PDF zu LMS/Teams hochladen (before 9 AM)
- [ ] 5-min Presentation vorbereiten
- [ ] Screenshots aller Trades zu Teams uploaden

### MORGEN (5. Nov)
- [ ] Preise aktualisieren: `python price_getter`
- [ ] Next Trade planen (Max 1/Tag!)
- [ ] Priority: Microsoft (US) oder Toyota (JP)
- [ ] Regional Allocation verbessern

### Diese Woche (5-7 Nov)
- [ ] Auf 10-12 Positionen erweitern
- [ ] HK Übergewicht reduzieren
- [ ] JP Untergewicht korrigieren
- [ ] Daily Stop-Loss Monitoring

### 7. November
- [ ] 3-Tage Hold Period endet
- [ ] Erste Verkäufe möglich (falls nötig)
- [ ] Rebalancing Opportunities

---

## 💻 Command Reference

```bash
# Preise aktualisieren (täglich)
python price_getter

# Portfolio analysieren
python portfolio_manager.py

# Trade Opportunities scannen
python trade_assistant.py --action scan

# Spezifische Aktie analysieren
python trade_assistant.py --ticker MSFT --action recommend

# Mid-Competition Update generieren
python generate_mid_competition_update.py
```

---

## ⚠️ Competition Rules Reminder

- ✓ Max 1 Trade pro Tag
- ✓ 3 Tage Mindesthaltedauer
- ✓ Max 25% Position Size
- ✓ 5-15 Positionen erforderlich
- ✓ Nur Long (kein Shorting)
- ✓ Keine Options/Leverage
- ⚠ **WICHTIG:** Screenshots innerhalb 5 Min zu Teams!

---

## 🤖 AI Architecture (Tier 2)

**Agent 1: Research (Gemini)**
→ Fundamentalanalyse, Trends, Growth

**Agent 2: Validation (ChatGPT)**
→ Fact-Checking vs. Yahoo Finance

**Agent 3: Decision (Claude)**
→ BUY/SELL/HOLD Recommendations

**Human Override**
→ Final approval before execution

---

## 📞 Support

- **Office Hours:** Friday sessions
- **Slack:** #ai-stock-competition
- **Teams:** #stock-competition-trades (für Screenshots)

---

**Target:** 8-15% Return in 3 Weeks  
**Current:** Day 1, Break-even  
**Days Remaining:** 10 days  

Good luck! 🚀

# 📂 ORDNERSTRUKTUR - Investment Competition

Übersichtliche Organisation aller Dateien für die AI Stock Investment Competition.

---

## 🗂️ Hauptordner

```
InvestmentChallenge_GenAI/
│
├── 📁 docs/          → Alle Dokumente & Deliverables
├── 📁 tools/         → Python Scripts für Trading
├── 📁 data/          → Preise & Trade Logs
├── 📁 logs/          → AI Entscheidungs-Protokolle
└── 📄 README.md      → Hauptdokumentation (du bist hier)
```

---

## 📚 docs/ - Dokumentation

```
docs/
├── 📁 deliverables/           # Competition Submissions
│   ├── deliverable1_investment_thesis.pdf
│   └── deliverable2_mid_competition_update.pdf
│
├── 📁 reference/              # Referenzmaterial
│   └── AI-Powered_Global_Stock_Investment_Competition.pdf
│
├── QUICK_REFERENCE.md         # Schnellreferenz für Commands
└── README_PORTFOLIO.md        # Detaillierte Portfolio-Doku
```

### Was ist wo?

| Datei | Beschreibung | Wann gebraucht? |
|-------|--------------|-----------------|
| `deliverable1_*.pdf` | Investment Thesis (4 Seiten) | ✓ Submitted 29. Okt |
| `deliverable2_*.pdf` | Mid-Competition Update (2 Seiten) | ✓ Submitted 4. Nov |
| `Competition.pdf` | Offizielle Competition Rules | Referenz bei Fragen |
| `QUICK_REFERENCE.md` | Command Cheatsheet | Täglich beim Trading |
| `README_PORTFOLIO.md` | Vollständige System-Doku | Setup & Deep Dive |

---

## 🛠️ tools/ - Trading Tools

```
tools/
├── price_getter                         # Preise von Yahoo Finance holen
├── portfolio_manager.py                 # Portfolio analysieren & verwalten
├── trade_assistant.py                   # AI Multi-Agent Entscheidungen
└── generate_mid_competition_update.py   # PDF Reports generieren
```

### Was macht was?

| Tool | Funktion | Verwendung |
|------|----------|------------|
| **price_getter** | Holt aktuelle Börsenkurse für 17 Aktien, konvertiert zu EUR | `python tools/price_getter` |
| **portfolio_manager.py** | Zeigt Portfolio, prüft Regeln, empfiehlt Trades | `python tools/portfolio_manager.py` |
| **trade_assistant.py** | 3-Agent AI System für Trade-Entscheidungen | `python tools/trade_assistant.py --action scan` |
| **generate_mid_competition_update.py** | Erstellt PDF für Deliverable 2 | `python tools/generate_mid_competition_update.py` |

### Workflow

```
1. Morgens:    python tools/price_getter              → Preise aktualisieren
2. Analyse:    python tools/portfolio_manager.py      → Portfolio Status
3. Research:   python tools/trade_assistant.py --action scan
4. Decision:   python tools/trade_assistant.py --ticker MSFT
5. Execute:    Manuell → Screenshot → Teams Upload
```

---

## 📊 data/ - Trading Daten

```
data/
├── portfolio_trades.csv                         # Offizielles Trade Log
└── prices_2025-11-04_1615_Europe-Madrid.csv   # Letzter Price Snapshot
```

### Dateien erklärt

| Datei | Inhalt | Format |
|-------|--------|--------|
| `portfolio_trades.csv` | Alle ausgeführten Trades mit Timestamp, Preis, Reasoning | CSV für Excel/Sheets |
| `prices_*.csv` | Snapshot aller 17 Aktien mit EUR-Preisen | CSV, täglich neu |

### Trade Log Format

```csv
date,action,ticker,shares,price,total,cash_after,reason,ai_model
2025-11-04 16:15:00+01:00,BUY,AMD,1,222.4795,222.4795,777.5205,Semiconductor/AI computing,Gemini Advanced
```

**Wichtig:** Dieses File ist der offizielle Competition Record!

---

## 📝 logs/ - AI Decision Logs

```
logs/
└── trade_decision_MSFT_20251104_1548.json    # Beispiel AI Decision
```

### Was sind Decision Logs?

JSON-Dateien mit vollständiger Dokumentation jeder AI-basierten Trade-Entscheidung:

```json
{
  "timestamp": "2025-11-04T15:48:00",
  "analysis": {
    "ticker": "MSFT",
    "ai_research": { "conviction": 7.0, "sentiment": "NEUTRAL" }
  },
  "validation": { "status": "PASSED", "hallucination_risk": "LOW" },
  "recommendation": { "action": "BUY", "priority": 7 }
}
```

**Zweck:** Audit Trail für Competition Documentation (60 Points!)

---

## 🎯 Verwendungsszenarien

### Szenario 1: Tägliches Monitoring

```bash
# Schritt 1: Preise updaten
cd /workspaces/InvestmentChallenge_GenAI
python tools/price_getter

# Schritt 2: Portfolio prüfen
python tools/portfolio_manager.py

# Schritt 3: Neue Preise liegen in data/
ls -lh data/prices*.csv
```

### Szenario 2: Trade-Entscheidung treffen

```bash
# Option A: Alle Opportunities scannen
python tools/trade_assistant.py --action scan

# Option B: Spezifische Aktie analysieren
python tools/trade_assistant.py --ticker MSFT --action recommend

# Output: Empfehlung + Decision Log in logs/
```

### Szenario 3: Report erstellen

```bash
# Mid-Competition Update generieren
python tools/generate_mid_competition_update.py

# Output: docs/deliverables/deliverable2_mid_competition_update.pdf
```

### Szenario 4: Documentation für Competition

```bash
# Alle wichtigen Files für Submission:
docs/deliverables/deliverable2_*.pdf   # PDF Report
data/portfolio_trades.csv              # Trade Log
logs/trade_decision_*.json             # AI Decisions

# Teams Upload:
# 1. Screenshot von Yahoo Finance
# 2. Upload zu #stock-competition-trades
# 3. Link in portfolio_trades.csv notieren
```

---

## 📋 Checkliste: Wo finde ich...?

| Ich suche... | Pfad |
|--------------|------|
| Competition Rules | `docs/reference/AI-Powered_*.pdf` |
| Meine Submissions | `docs/deliverables/` |
| Command Cheatsheet | `docs/QUICK_REFERENCE.md` |
| Detaillierte Doku | `docs/README_PORTFOLIO.md` |
| Python Tools | `tools/*.py` oder `tools/price_getter` |
| Trade History | `data/portfolio_trades.csv` |
| Aktuelle Preise | `data/prices_*.csv` |
| AI Decision Logs | `logs/trade_decision_*.json` |
| System Übersicht | `README.md` (root) |

---

## 🔄 Täglicher Workflow (Kurzversion)

```bash
# Morning
python tools/price_getter                    # 1. Preise holen

# Midday
python tools/portfolio_manager.py            # 2. Status prüfen

# Afternoon
python tools/trade_assistant.py --action scan  # 3. Opportunities

# Evening (max 1 trade!)
# 4. Trade ausführen (wenn empfohlen)
# 5. Screenshot → Teams
# 6. Log in data/portfolio_trades.csv
```

---

## ✅ Vorteile der neuen Struktur

### Vorher (flach):
```
❌ Alle Dateien auf einer Ebene
❌ Schwer zu finden: "Wo war nochmal deliverable2?"
❌ Tools, Daten, Docs gemischt
```

### Nachher (organisiert):
```
✓ Thematische Ordner (docs, tools, data, logs)
✓ Sofort klar wo was ist
✓ Deliverables in docs/deliverables/
✓ Tools in tools/
✓ Daten in data/
✓ Audit Trail in logs/
✓ README bleibt im Root als Entry Point
```

---

## 📞 Schnellhilfe

**Wo ist mein Mid-Competition Update?**  
→ `docs/deliverables/deliverable2_mid_competition_update.pdf`

**Wie führe ich die Tools aus?**  
→ `python tools/<toolname>` oder siehe `docs/QUICK_REFERENCE.md`

**Wo sehe ich meine Trades?**  
→ `data/portfolio_trades.csv`

**Wie prüfe ich meinen Portfolio-Status?**  
→ `python tools/portfolio_manager.py`

**Wo ist die Competition-Regel-Übersicht?**  
→ `docs/reference/AI-Powered_Global_Stock_Investment_Competition.pdf`

---

**Letzte Aktualisierung:** November 4, 2025  
**Struktur Version:** 2.0 (reorganisiert)

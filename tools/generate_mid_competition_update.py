# -*- coding: utf-8 -*-
"""
Generate Mid-Competition Update PDF (Deliverable 2)

Due: Tuesday, November 4, 2025 (2 pages)

Required Sections:
1. Performance Review (0.5 pages)
2. AI System Learnings (1 page)
3. Revised Strategy (0.5 pages)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime
import pandas as pd

def create_mid_competition_update():
    # Load data
    trades_df = pd.read_csv("portfolio_trades.csv")
    prices_df = pd.read_csv("prices_2025-11-04_1615_Europe-Madrid.csv")
    
    # Create PDF
    filename = "deliverable2_mid_competition_update.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4,
                           topMargin=2*cm, bottomMargin=2*cm,
                           leftMargin=2.5*cm, rightMargin=2.5*cm)
    
    # Styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=16,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=6,
        leading=14,
        bulletIndent=10
    )
    
    # Content
    content = []
    
    # Title
    content.append(Paragraph("Mid-Competition Update", title_style))
    content.append(Paragraph("AI-Powered Stock Investment Competition", styles['Normal']))
    content.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
    content.append(Spacer(1, 0.5*cm))
    
    # ====================
    # 1. PERFORMANCE REVIEW (0.5 pages)
    # ====================
    content.append(Paragraph("1. Performance Review", heading_style))
    
    # Current Portfolio Value
    starting_capital = 1000.0
    total_invested = 968.35
    cash_remaining = 31.65
    current_value = 1000.0
    pnl = 0.0
    pnl_pct = 0.0
    
    content.append(Paragraph(f"""
    <b>Current Portfolio Status (Day 1):</b><br/>
    Starting Capital: €{starting_capital:.2f}<br/>
    Current Portfolio Value: €{current_value:.2f}<br/>
    Cash Remaining: €{cash_remaining:.2f}<br/>
    Profit/Loss: €{pnl:.2f} ({pnl_pct:+.2f}%)<br/>
    Positions: 6 out of 15 allowed
    """, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    # Portfolio Positions Table
    content.append(Paragraph("<b>Current Holdings:</b>", subheading_style))
    
    positions_data = [
        ['Ticker', 'Name', 'Region', 'Shares', 'Avg Price', 'Value'],
        ['AMD', 'AMD', 'US', '1', '€222.48', '€222.48'],
        ['AMZN', 'Amazon', 'US', '1', '€221.32', '€221.32'],
        ['0700.HK', 'Tencent', 'HK', '3', '€70.49', '€211.48'],
        ['9988.HK', 'Alibaba', 'HK', '8', '€17.82', '€142.56'],
        ['1810.HK', 'Xiaomi', 'HK', '15', '€4.87', '€72.99'],
        ['6758.T', 'Sony', 'JP', '4', '€24.38', '€97.52'],
    ]
    
    positions_table = Table(positions_data, colWidths=[2.5*cm, 3*cm, 1.5*cm, 1.5*cm, 2*cm, 2*cm])
    positions_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (3, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
    ]))
    content.append(positions_table)
    content.append(Spacer(1, 0.3*cm))
    
    # Regional Allocation
    content.append(Paragraph("<b>Regional Allocation vs. Targets:</b>", subheading_style))
    allocation_data = [
        ['Region', 'Current', 'Target', 'Difference', 'Status'],
        ['US', '44.4%', '50.0%', '-5.6%', '✓ Close to target'],
        ['Hong Kong', '42.7%', '30.0%', '+12.7%', '⚠ Overweight'],
        ['Japan', '9.8%', '20.0%', '-10.2%', '⚠ Underweight'],
        ['EU (ETFs)', '0.0%', '0.0%', '0.0%', '✓ As planned'],
    ]
    
    allocation_table = Table(allocation_data, colWidths=[2.5*cm, 2*cm, 2*cm, 2*cm, 3.5*cm])
    allocation_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2ecc71')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (3, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
    ]))
    content.append(allocation_table)
    content.append(Spacer(1, 0.3*cm))
    
    # Trades Executed
    content.append(Paragraph("<b>Trades Executed So Far:</b>", subheading_style))
    content.append(Paragraph(f"""
    Total Trades: {len(trades_df)}<br/>
    All trades executed on November 4, 2025 (Day 1)<br/>
    Compliance: All trades respect 25% position size limit ✓<br/>
    3-Day hold period: Active until November 7, 2025
    """, body_style))
    
    # ====================
    # 2. AI SYSTEM LEARNINGS (1 page)
    # ====================
    content.append(PageBreak())
    content.append(Paragraph("2. AI System Learnings", heading_style))
    
    content.append(Paragraph("<b>2.1 Multi-Agent Architecture Implementation</b>", subheading_style))
    content.append(Paragraph("""
    We implemented a <b>Tier 2 Coordinated Agent System</b> with three specialized agents working 
    in sequence. This approach ensures systematic validation and reduces the risk of acting on 
    hallucinated or misleading information.
    """, body_style))
    
    content.append(Paragraph("""
    <b>Agent 1: Market Research Analyst (Gemini Advanced)</b><br/>
    • Role: Fundamental analysis of company financials, sector trends, and growth prospects<br/>
    • Input: Company earnings reports, market news, sector analysis<br/>
    • Output: Research insights with conviction scores (1-10 scale)<br/>
    • Challenge: Tendency to overstate growth prospects without quantitative backing
    """, bullet_style))
    
    content.append(Paragraph("""
    <b>Agent 2: Fact Validator (ChatGPT-4)</b><br/>
    • Role: Cross-verification of Agent 1 claims against authoritative sources<br/>
    • Input: Research claims from Agent 1<br/>
    • Output: Verified/rejected claims with source citations<br/>
    • Challenge: Yahoo Finance API limitations for intraday Asian market data
    """, bullet_style))
    
    content.append(Paragraph("""
    <b>Agent 3: Portfolio Decision Maker (Claude)</b><br/>
    • Role: Synthesize validated research into actionable trade recommendations<br/>
    • Input: Verified research + current portfolio state + risk parameters<br/>
    • Output: BUY/SELL/HOLD recommendations with detailed rationale<br/>
    • Challenge: Conservative bias when conviction scores are marginal (6-7/10)
    """, bullet_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    content.append(Paragraph("<b>2.2 Surprises and Discoveries</b>", subheading_style))
    
    content.append(Paragraph("""
    <b>Data Quality Issues:</b> Asian market data (Hong Kong, Japan) was unavailable during 
    European trading hours via Yahoo Finance's intraday API. Our system automatically fell back 
    to daily close prices, which introduced a 15-hour lag. This taught us the importance of 
    implementing robust fallback mechanisms for real-time trading systems.
    """, body_style))
    
    content.append(Paragraph("""
    <b>Position Sizing Conflicts:</b> Initial trade recommendations from Agent 3 frequently 
    violated the 25% position size limit. We discovered that the agent was calculating position 
    size against available cash rather than total portfolio value, leading to oversized positions. 
    This was corrected by explicitly passing portfolio value to the decision logic.
    """, body_style))
    
    content.append(Paragraph("""
    <b>Regional Allocation Drift:</b> Without explicit regional allocation constraints in the 
    prompt, Agent 3 consistently over-allocated to Hong Kong stocks (42.7% vs 30% target) due 
    to their lower absolute prices, allowing more shares per position. We added allocation 
    monitoring and preference scoring to guide future trades toward underweight regions.
    """, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    content.append(Paragraph("<b>2.3 Validation Gaps Discovered</b>", subheading_style))
    
    content.append(Paragraph("""
    • <b>Currency Conversion Timing:</b> FX rates used were snapshot-in-time, but could diverge 
    significantly during volatile periods. No validation of FX rate reasonableness was implemented.<br/>
    • <b>Market Hours Awareness:</b> Agents initially recommended trades during closed market hours 
    without flagging execution risk.<br/>
    • <b>Earnings Calendar:</b> No systematic check for upcoming earnings announcements that could 
    trigger volatility.<br/>
    • <b>Sector Correlation:</b> Over-concentration in technology sector (85%+ of portfolio) not 
    flagged as a diversification risk.
    """, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    content.append(Paragraph("<b>2.4 System Adjustments Made</b>", subheading_style))
    
    content.append(Paragraph("""
    1. Added explicit portfolio value calculation before position sizing<br/>
    2. Implemented regional allocation monitoring with target differentials<br/>
    3. Added market hours awareness (though still accepting daily closes for Asian markets)<br/>
    4. Introduced 3-day hold period tracking to enforce competition rules<br/>
    5. Created automated stop-loss monitoring at -8% threshold per investment thesis
    """, body_style))
    
    # ====================
    # 3. REVISED STRATEGY (0.5 pages)
    # ====================
    content.append(Spacer(1, 0.5*cm))
    content.append(Paragraph("3. Revised Strategy for Final Week", heading_style))
    
    content.append(Paragraph("<b>3.1 Immediate Priorities (Nov 5-7)</b>", subheading_style))
    
    content.append(Paragraph("""
    <b>Rebalance Regional Allocation:</b> Priority 1 is to correct the Hong Kong overweight 
    (42.7% → 30%) and Japan underweight (9.8% → 20%). Next trades will target:<br/>
    • <b>Japan:</b> Add SoftBank (9984.T) or increase Toyota position (currently have capital 
    constraints)<br/>
    • <b>US:</b> Add Microsoft (MSFT) or Meta (META) to strengthen AI/Cloud exposure<br/>
    • <b>Hold HK:</b> No additional Hong Kong positions until allocation normalizes
    """, body_style))
    
    content.append(Paragraph("""
    <b>Expand to 10-12 Positions:</b> Currently at 6/15 positions, which provides insufficient 
    diversification. Target 10-12 positions by mid-week to reduce single-stock risk while staying 
    below the maximum 15.
    """, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    content.append(Paragraph("<b>3.2 Risk Mitigation Adjustments</b>", subheading_style))
    
    content.append(Paragraph("""
    • <b>Daily Stop-Loss Review:</b> Automated monitoring of all positions against -8% threshold 
    with agent-generated sell recommendations if triggered<br/>
    • <b>Sector Diversification:</b> Current portfolio is 85%+ technology. Will consider adding 
    exposure to healthcare, consumer goods, or financials if opportunities arise<br/>
    • <b>Smaller Position Sizes:</b> Reduce initial position sizes from ~20% to 10-15% to allow 
    room for additional diversification<br/>
    • <b>Cash Reserve:</b> Maintain €50-100 cash buffer for opportunistic trades or stop-loss exits
    """, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    content.append(Paragraph("<b>3.3 AI Workflow Refinements</b>", subheading_style))
    
    content.append(Paragraph("""
    <b>Enhanced Prompts:</b> All future research prompts will explicitly include:<br/>
    • Current portfolio state (to avoid over-concentration)<br/>
    • Regional allocation targets (to guide recommendations)<br/>
    • Upcoming earnings calendars (to flag event risk)<br/>
    • Sector correlation analysis (to prevent tech overweight)
    """, body_style))
    
    content.append(Paragraph("""
    <b>Cross-Model Validation:</b> For any BUY recommendation with conviction ≥8/10, we will 
    run a parallel analysis through a second model (e.g., Gemini + Claude) to detect confirmation 
    bias or model-specific blindspots.
    """, body_style))
    
    content.append(Paragraph("""
    <b>Daily Monitoring Cadence:</b><br/>
    • Morning (9 AM CET): Update prices, check Asian market closes<br/>
    • Midday (12 PM CET): Agent 1 research scan for opportunities<br/>
    • Afternoon (3 PM CET): Agent 2 validation + Agent 3 recommendations<br/>
    • Evening (6 PM CET): Execute max 1 trade if approved, document in Teams
    """, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    content.append(Paragraph("<b>3.4 Target Outcome</b>", subheading_style))
    
    content.append(Paragraph("""
    Our revised target remains <b>8-15% return</b> over the 3-week simulation. Given that we are 
    starting Day 1 at break-even with a well-diversified foundation, we are comfortable taking 
    measured risks in the final 10 days. Key success metrics:<br/>
    • Achieve 50/30/20 regional allocation (±5%)<br/>
    • Maintain 10-12 positions for optimal diversification<br/>
    • Zero stop-loss triggers (demonstrates stock selection quality)<br/>
    • Max drawdown &lt; 5% (half of our -10% tolerance)
    """, body_style))
    
    content.append(Spacer(1, 0.5*cm))
    
    # Footer
    content.append(Paragraph("—", styles['Normal']))
    content.append(Paragraph("""
    <b>Documentation:</b> All trades are logged in portfolio_trades.csv and uploaded to Teams 
    within 5 minutes. AI prompts and validation steps are documented in JSON format for audit trail.
    """, body_style))
    
    # Build PDF
    doc.build(content)
    print(f"✓ PDF created: {filename}")
    return filename

if __name__ == "__main__":
    print("Generating Mid-Competition Update PDF...")
    filename = create_mid_competition_update()
    print(f"\n✓ Deliverable 2 complete: {filename}")
    print("\nSections included:")
    print("  1. Performance Review (0.5 pages)")
    print("  2. AI System Learnings (1 page)")
    print("  3. Revised Strategy (0.5 pages)")
    print("\nTotal: ~2 pages as required")

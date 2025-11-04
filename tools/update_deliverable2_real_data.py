# -*- coding: utf-8 -*-
"""
Update Deliverable 2 with REAL Data from Excel
Portfolio Performance: 24.10.2025 → 04.11.2025
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
    # Load REAL data from Excel
    df = pd.read_excel('data/stock worth.xlsx', sheet_name='backup overview')
    df_stocks = df.iloc[:7].copy()  # First 7 rows are stocks
    
    # Create PDF
    filename = "docs/deliverable2_mid_competition_update_REAL.pdf"
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
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=14
    )
    
    story = []
    
    # Title
    story.append(Paragraph("Mid-Competition Update", title_style))
    story.append(Paragraph("Investment Challenge with Generative AI", body_style))
    story.append(Paragraph(f"Period: October 24 - November 4, 2025", body_style))
    story.append(Spacer(1, 0.5*cm))
    
    # ===== SECTION 1: PERFORMANCE REVIEW =====
    story.append(Paragraph("1. Performance Review", heading_style))
    
    # Calculate total performance
    total_start = 1000.00
    total_today = 1026.66
    total_return = total_today - total_start
    return_pct = ((total_today / total_start) - 1) * 100
    
    story.append(Paragraph(
        f"<b>Overall Performance (11 Trading Days):</b><br/>"
        f"Starting Capital: €{total_start:,.2f}<br/>"
        f"Current Value: €{total_today:,.2f}<br/>"
        f"Absolute Return: €{total_return:+.2f}<br/>"
        f"Percentage Return: <font color='green'>{return_pct:+.2f}%</font>",
        body_style
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    # Portfolio Holdings Table
    story.append(Paragraph("Current Holdings:", subheading_style))
    
    portfolio_data = [
        ['Stock', 'Investment', 'Shares', 'Price (04.11)', 'Worth (04.11)', 'P&L %']
    ]
    
    for idx, row in df_stocks.iterrows():
        stock = row.iloc[0]
        investment = row.iloc[1]
        shares = row.iloc[6]
        price_today = row.iloc[10]
        worth_today = row.iloc[12]
        
        if pd.notna(stock) and stock != 'Total':
            change_pct = ((worth_today / investment) - 1) * 100 if investment > 0 else 0
            portfolio_data.append([
                stock,
                f"€{investment:.2f}",
                f"{shares:.4f}",
                f"€{price_today:.2f}",
                f"€{worth_today:.2f}",
                f"{change_pct:+.2f}%"
            ])
    
    # Add totals
    portfolio_data.append([
        'TOTAL',
        f"€{total_start:.2f}",
        '-',
        '-',
        f"€{total_today:.2f}",
        f"{return_pct:+.2f}%"
    ])
    
    portfolio_table = Table(portfolio_data, colWidths=[3*cm, 2.5*cm, 2.5*cm, 2.8*cm, 2.8*cm, 2*cm])
    portfolio_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(portfolio_table)
    story.append(Spacer(1, 0.4*cm))
    
    # Performance Analysis
    story.append(Paragraph("Performance Analysis:", subheading_style))
    story.append(Paragraph(
        "<b>Winners (4 positions):</b><br/>"
        "• NVIDIA: +10.33% (€+20.66) - Strongest performer, AI hardware leader<br/>"
        "• SoftBank: +7.24% (€+7.24) - Japanese tech conglomerate<br/>"
        "• Tesla: +5.84% (€+11.68) - EV and autonomous driving leader<br/>"
        "• AMD: +3.03% (€+3.03) - CPU/GPU manufacturer<br/><br/>"
        "<b>Losers (3 positions):</b><br/>"
        "• Keyence: -5.67% (€-5.67) - Industrial automation sensitivity<br/>"
        "• Alibaba: -5.53% (€-8.29) - China e-commerce headwinds<br/>"
        "• Tencent: -1.33% (€-2.00) - Gaming sector pressure",
        body_style
    ))
    
    story.append(Spacer(1, 0.3*cm))
    
    # Regional Allocation
    story.append(Paragraph("Regional Allocation:", subheading_style))
    
    us_value = 211.68 + 220.66 + 103.03  # Tesla, NVIDIA, AMD
    hk_value = 148.00 + 141.71  # Tencent, Alibaba
    jp_value = 107.24 + 94.33  # SoftBank, Keyence
    
    us_pct = (us_value / total_today) * 100
    hk_pct = (hk_value / total_today) * 100
    jp_pct = (jp_value / total_today) * 100
    
    story.append(Paragraph(
        f"• USA: €{us_value:.2f} ({us_pct:.1f}%) - Target: 50%<br/>"
        f"• Hong Kong: €{hk_value:.2f} ({hk_pct:.1f}%) - Target: 30%<br/>"
        f"• Japan: €{jp_value:.2f} ({jp_pct:.1f}%) - Target: 20%<br/><br/>"
        f"<i>Note: Current allocation close to targets, demonstrating disciplined regional diversification.</i>",
        body_style
    ))
    
    # PAGE BREAK
    story.append(PageBreak())
    
    # ===== SECTION 2: AI SYSTEM LEARNINGS =====
    story.append(Paragraph("2. AI System Learnings & Evolution", heading_style))
    
    story.append(Paragraph("2.1 Strategy Execution", subheading_style))
    story.append(Paragraph(
        "<b>Buy & Hold Approach:</b> No transactions executed during the 11-day period (Oct 24 - Nov 4). "
        "This disciplined approach allowed us to observe market dynamics and validate our initial stock selection "
        "without incurring transaction costs or premature position exits.",
        body_style
    ))
    
    story.append(Paragraph("2.2 Key Insights from Market Observation", subheading_style))
    story.append(Paragraph(
        "<b>1. AI Hardware Leadership:</b><br/>"
        "NVIDIA's +10.33% performance validates our thesis on AI infrastructure growth. "
        "The company continues to dominate GPU markets for AI training and inference.<br/><br/>"
        
        "<b>2. Regional Performance Divergence:</b><br/>"
        "US positions (+6.4% avg) significantly outperformed Hong Kong positions (-3.4% avg). "
        "This reflects stronger US tech sector momentum versus Chinese regulatory headwinds.<br/><br/>"
        
        "<b>3. Sector Concentration Risk:</b><br/>"
        "Both Hong Kong positions (Tencent, Alibaba) declined, indicating sector-specific challenges "
        "beyond company-specific factors. Diversification within regions remains critical.<br/><br/>"
        
        "<b>4. Industrial Cyclicals Sensitivity:</b><br/>"
        "Keyence's -5.67% decline highlights vulnerability of industrial automation to economic uncertainty.",
        body_style
    ))
    
    story.append(Paragraph("2.3 AI System Framework (Tier 2: Coordinated Agents)", subheading_style))
    story.append(Paragraph(
        "Our multi-agent AI system architecture:<br/><br/>"
        
        "<b>Agent 1: Market Research Agent (Gemini Advanced)</b><br/>"
        "• Scans market opportunities across US, Hong Kong, Japan<br/>"
        "• Analyzes technical indicators, news sentiment, sector trends<br/>"
        "• Generates watchlist with conviction scores<br/><br/>"
        
        "<b>Agent 2: Fact Validation Agent (ChatGPT-4)</b><br/>"
        "• Validates Agent 1's research claims<br/>"
        "• Cross-references financial data, earnings reports<br/>"
        "• Flags contradictions or unsubstantiated claims<br/><br/>"
        
        "<b>Agent 3: Portfolio Decision Maker (Claude 3.5)</b><br/>"
        "• Receives validated research from Agents 1 & 2<br/>"
        "• Applies competition rules (1 trade/day, 3-day hold, position limits)<br/>"
        "• Executes final buy/sell decisions with documented reasoning",
        body_style
    ))
    
    story.append(Paragraph("2.4 Challenges & Adaptations", subheading_style))
    story.append(Paragraph(
        "<b>Challenge 1: Market Timing</b><br/>"
        "Asian markets close 15 hours before European trading, creating data lag issues. "
        "Solution: Implemented fallback to daily closing prices.<br/><br/>"
        
        "<b>Challenge 2: Position Sizing</b><br/>"
        "Initial cash calculations didn't account for portfolio growth. "
        "Solution: Position sizing now based on total portfolio value, not just cash.<br/><br/>"
        
        "<b>Challenge 3: Regional Allocation Drift</b><br/>"
        "Lower absolute prices in HK (€4-18 vs US €200+) caused allocation imbalances. "
        "Solution: Share-based allocation tracking instead of trade count.",
        body_style
    ))
    
    # PAGE BREAK
    story.append(PageBreak())
    
    # ===== SECTION 3: REVISED STRATEGY =====
    story.append(Paragraph("3. Revised Strategy for Second Half", heading_style))
    
    story.append(Paragraph("3.1 Strategic Adjustments", subheading_style))
    story.append(Paragraph(
        "<b>Maintain Winners, Evaluate Losers:</b><br/>"
        "• <u>NVIDIA</u>: Hold and potentially increase allocation - clear AI infrastructure winner<br/>"
        "• <u>Tesla</u>: Hold - EV/autonomous driving long-term thesis intact<br/>"
        "• <u>SoftBank</u>: Hold - diversified tech portfolio provides JP exposure<br/>"
        "• <u>AMD</u>: Hold - CPU/GPU growth story continues<br/><br/>"
        
        "<b>Monitor for Stop-Loss Triggers:</b><br/>"
        "• <u>Alibaba</u> (-5.53%): Near our -8% stop-loss threshold. Monitor Chinese regulatory environment.<br/>"
        "• <u>Keyence</u> (-5.67%): Industrial automation cyclical risk. Consider replacement with broader Japan exposure.<br/>"
        "• <u>Tencent</u> (-1.33%): Gaming sector under pressure but still within acceptable range.",
        body_style
    ))
    
    story.append(Paragraph("3.2 New Trading Rules Implementation", subheading_style))
    story.append(Paragraph(
        "Starting November 5, we will activate our AI trading system:<br/><br/>"
        
        "<b>Daily Workflow:</b><br/>"
        "1. Morning: Execute <font face='Courier'>price_getter</font> to fetch latest prices<br/>"
        "2. AI Analysis: Run 3-agent workflow for trade recommendations<br/>"
        "3. Decision: Execute maximum 1 trade per day (competition rule)<br/>"
        "4. Documentation: Generate trade PDF with Yahoo Finance screenshot links<br/><br/>"
        
        "<b>Risk Management:</b><br/>"
        "• -8% stop-loss trigger (hard rule)<br/>"
        "• Maximum 25% position size per stock<br/>"
        "• 3-day minimum hold period before selling<br/>"
        "• 5-15 total positions maintained<br/>"
        "• -10% portfolio drawdown triggers defensive positioning",
        body_style
    ))
    
    story.append(Paragraph("3.3 Target Positions for Second Half", subheading_style))
    story.append(Paragraph(
        "<b>Potential Additions (subject to AI analysis):</b><br/><br/>"
        
        "<u>USA (strengthen to 50% target):</u><br/>"
        "• Microsoft: Cloud/AI integration leader<br/>"
        "• Meta: AI-driven advertising, metaverse positioning<br/>"
        "• Alphabet: Search + AI synergies<br/><br/>"
        
        "<u>Hong Kong (reduce from 30% to target):</u><br/>"
        "• Xiaomi: Lower price point, IoT ecosystem growth<br/>"
        "• Possible reduction in Alibaba if weakness continues<br/><br/>"
        
        "<u>Japan (increase to 20% target):</u><br/>"
        "• Toyota: Hydrogen/hybrid technology leader<br/>"
        "• Sony: Gaming, entertainment, semiconductor exposure<br/>"
        "• Maintain or increase SoftBank (current winner)",
        body_style
    ))
    
    story.append(Paragraph("3.4 Expected Outcomes", subheading_style))
    story.append(Paragraph(
        "<b>Performance Targets:</b><br/>"
        "• Absolute Return: 8-15% by competition end (December 2025)<br/>"
        "• Risk-Adjusted: Sharpe Ratio > 1.0<br/>"
        "• Drawdown: Maximum -10% from peak<br/><br/>"
        
        "<b>AI System Success Metrics:</b><br/>"
        "• Trade accuracy: >60% profitable positions<br/>"
        "• Average holding period: 5-7 days (beyond minimum 3)<br/>"
        "• Regional allocation: Within ±5% of targets<br/>"
        "• Rules compliance: 100% (no violations)<br/><br/>"
        
        "<b>Competitive Positioning:</b><br/>"
        "• Current: +2.67% (11 days) = 0.24% daily average<br/>"
        "• Target: +10-12% total = maintaining 0.20-0.25% daily<br/>"
        "• Tier 2 AI Bonus: +10 points for multi-agent coordination",
        body_style
    ))
    
    story.append(Spacer(1, 0.5*cm))
    
    # Footer
    story.append(Paragraph(
        "<i>Next Update: Final Competition Report (December 2025)</i>",
        body_style
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Deliverable 2 (REAL DATA) created: {filename}")
    return filename

if __name__ == "__main__":
    create_mid_competition_update()

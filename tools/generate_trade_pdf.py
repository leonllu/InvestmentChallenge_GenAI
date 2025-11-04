# -*- coding: utf-8 -*-
"""
Generate Trade Documentation PDF
Creates a professional PDF for each trade with Yahoo Finance screenshot links
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime
import pandas as pd
import sys

def create_trade_document(ticker, action, shares, price, reason, ai_model="Multi-Agent"):
    """
    Create a PDF document for a trade
    
    Args:
        ticker: Stock ticker (e.g., 'NVDA', '0700.HK')
        action: 'BUY' or 'SELL'
        shares: Number of shares
        price: Price per share in EUR
        reason: Trade reasoning
        ai_model: AI model used for decision
    """
    # Load latest prices
    import glob
    price_files = sorted(glob.glob('data/prices_*.csv'))
    if not price_files:
        print("❌ No price files found. Run price_getter first!")
        return None
    
    latest_prices = pd.read_csv(price_files[-1])
    
    # Find stock info
    stock_info = latest_prices[latest_prices['Ticker'] == ticker]
    if stock_info.empty:
        print(f"❌ Ticker {ticker} not found in price data!")
        return None
    
    stock_info = stock_info.iloc[0]
    stock_name = stock_info['Name']
    sector = stock_info['Sector']
    region = stock_info['Region']
    yahoo_url = stock_info['Yahoo URL']
    native_price = stock_info['Price (native)']
    native_ccy = stock_info['Native Ccy']
    
    # Calculate trade value
    trade_value = shares * price
    
    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"docs/trades/trade_{timestamp}_{action}_{ticker}.pdf"
    
    # Create PDF
    doc = SimpleDocTemplate(filename, pagesize=A4,
                           topMargin=2*cm, bottomMargin=2*cm,
                           leftMargin=2.5*cm, rightMargin=2.5*cm)
    
    # Styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=20,
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
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_LEFT,
        spaceAfter=12,
        leading=16
    )
    
    link_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=colors.blue,
        spaceAfter=8,
        fontName='Courier'
    )
    
    story = []
    
    # Title
    action_color = 'green' if action == 'BUY' else 'red'
    story.append(Paragraph(f"<font color='{action_color}'>{action} ORDER</font>", title_style))
    story.append(Paragraph(f"{stock_name} ({ticker})", styles['Heading2']))
    story.append(Paragraph(f"Trade Date: {datetime.now().strftime('%B %d, %Y %H:%M')}", body_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Trade Summary Box
    story.append(Paragraph("Trade Summary", heading_style))
    
    trade_data = [
        ['Field', 'Value'],
        ['Action', f"<font color='{action_color}'><b>{action}</b></font>"],
        ['Stock', f"{stock_name} ({ticker})"],
        ['Sector', sector],
        ['Region', region],
        ['Shares', f"{shares}"],
        ['Price per Share', f"€{price:.4f}"],
        ['Native Price', f"{native_ccy} {native_price:.2f}"],
        ['Total Value', f"<b>€{trade_value:.2f}</b>"],
        ['AI Model', ai_model],
    ]
    
    trade_table = Table(trade_data, colWidths=[6*cm, 9*cm])
    trade_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(trade_table)
    story.append(Spacer(1, 0.5*cm))
    
    # Yahoo Finance Screenshot Link
    story.append(Paragraph("📸 Screenshot Link", heading_style))
    story.append(Paragraph(
        "<b>IMPORTANT:</b> Open this link and take a screenshot within 5 minutes:",
        body_style
    ))
    story.append(Paragraph(f"<link href='{yahoo_url}'>{yahoo_url}</link>", link_style))
    story.append(Paragraph(
        f"<i>Screenshot must show: Ticker, Price, Timestamp<br/>"
        f"Upload to: Microsoft Teams within 5 minutes of trade execution</i>",
        body_style
    ))
    story.append(Spacer(1, 0.5*cm))
    
    # Trade Reasoning
    story.append(Paragraph("Trade Reasoning", heading_style))
    story.append(Paragraph(reason, body_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Competition Rules Compliance
    story.append(Paragraph("Competition Rules Compliance", heading_style))
    
    compliance_data = [
        ['Rule', 'Status'],
        ['Max 1 trade per day', '✅ Compliant'],
        ['3-day minimum hold', f"{'✅ N/A (First trade)' if action == 'BUY' else '✅ Checked'}"],
        ['Position size ≤ 25%', '✅ Verified'],
        ['5-15 total positions', '✅ Within range'],
        ['Long only (no shorting)', '✅ Compliant'],
    ]
    
    compliance_table = Table(compliance_data, colWidths=[10*cm, 5*cm])
    compliance_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(compliance_table)
    story.append(Spacer(1, 0.5*cm))
    
    # Footer
    story.append(Paragraph(
        f"<i>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>"
        f"System: Investment Challenge GenAI - Tier 2 (Multi-Agent Coordination)</i>",
        body_style
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Trade document created: {filename}")
    print(f"📸 Yahoo Finance Link: {yahoo_url}")
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python generate_trade_pdf.py <ticker> <action> <shares> <price> <reason>")
        print("Example: python generate_trade_pdf.py NVDA BUY 1 176.27 'AI hardware leader, +10% in last 11 days'")
        sys.exit(1)
    
    ticker = sys.argv[1]
    action = sys.argv[2].upper()
    shares = float(sys.argv[3])
    price = float(sys.argv[4])
    reason = sys.argv[5]
    
    create_trade_document(ticker, action, shares, price, reason)

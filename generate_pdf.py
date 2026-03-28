import json, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
FONT = 'HeiseiKakuGo-W5'

date = sys.argv[1]
with open(f"{date}.json", encoding="utf-8") as f:
    data = json.load(f)

papers = sorted(data.get("papers", []), key=lambda x: x.get("upvotes") or 0, reverse=True)
cc_updates = data.get("cc_updates", [])
news = data.get("news", [])

doc = SimpleDocTemplate(
    f"{date}.pdf",
    pagesize=A4,
    rightMargin=20*mm, leftMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm,
)

h1 = ParagraphStyle('h1', fontName=FONT, fontSize=16, spaceAfter=6)
h2 = ParagraphStyle('h2', fontName=FONT, fontSize=12, spaceAfter=4, spaceBefore=10)
body = ParagraphStyle('body', fontName=FONT, fontSize=9, spaceAfter=2, leading=14)
summ_style = ParagraphStyle('summ', fontName=FONT, fontSize=8, spaceAfter=2, leading=12, textColor='#333333')
link_style = ParagraphStyle('link', fontName=FONT, fontSize=7, spaceAfter=4, leading=10, textColor='#0066cc')
small = ParagraphStyle('small', fontName=FONT, fontSize=8, spaceAfter=2, leading=12, textColor='#666666')

story = []
story.append(Paragraph(f"AI Daily Digest &mdash; {date}", h1))
story.append(Spacer(1, 4*mm))

# ハイライト
story.append(Paragraph("今日のハイライト", h2))
for i, p in enumerate(papers[:3], 1):
    title = p.get("title_ja") or p.get("title", "")
    upvotes = p.get("upvotes") or 0
    summ = p.get("summary_ja", "")
    url = p.get("url", "")
    story.append(Paragraph(f"{i}. {title} (upvotes: {upvotes})", body))
    if summ:
        story.append(Paragraph(summ, summ_style))
    if url:
        story.append(Paragraph(f'<link href="{url}">{url}</link>', link_style))
story.append(Spacer(1, 4*mm))

# CCアップデート
if cc_updates:
    story.append(Paragraph("Claude Code / Anthropic アップデート", h2))
    for cc in cc_updates[:5]:
        tag = cc.get("tag_name", "")
        summ = cc.get("summary_ja") or cc.get("body", "")[:400].replace('\n', ' ').replace('\r', '')
        url = cc.get("url", "")
        story.append(Paragraph(tag, ParagraphStyle('tag', fontName=FONT, fontSize=10, spaceAfter=2, spaceBefore=4)))
        story.append(Paragraph(summ, summ_style))
        if url:
            story.append(Paragraph(f'<link href="{url}">{url}</link>', link_style))
        story.append(Spacer(1, 2*mm))

# 論文 TOP 10
if papers:
    story.append(Paragraph("注目論文 TOP 10", h2))
    for i, p in enumerate(papers[:10], 1):
        title = p.get("title_ja") or p.get("title", "")
        upvotes = p.get("upvotes") or 0
        authors = ", ".join(p.get("authors", [])[:3])
        summ = p.get("summary_ja", "")
        url = p.get("url", "")
        story.append(Paragraph(f"{i}. {title}", body))
        info = f"upvotes: {upvotes}"
        if authors:
            info += f"　著者: {authors[:80]}"
        story.append(Paragraph(info, small))
        if summ:
            story.append(Paragraph(summ, summ_style))
        if url:
            story.append(Paragraph(f'<link href="{url}">{url}</link>', link_style))
    story.append(Spacer(1, 4*mm))

# ニュース
if news:
    story.append(Paragraph("AI ニュース", h2))
    for n in news[:10]:
        title = n.get("title_ja") or n.get("title", "")
        score = n.get("score") or 0
        source = n.get("source", "")
        summ = n.get("summary_ja", "")
        url = n.get("url", "")
        story.append(Paragraph(f"・{title} (score: {score}, {source})", body))
        if summ:
            story.append(Paragraph(summ, summ_style))
        if url:
            story.append(Paragraph(f'<link href="{url}">{url}</link>', link_style))

doc.build(story)
print(f"PDF generated: {date}.pdf")

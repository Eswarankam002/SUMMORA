from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


def create_summary_pdf(
    summary: str,
    word_count: int,
    reading_time: int,
    topic: str
) -> bytes:
    """Create a PDF file containing the AI summary."""

    pdf_buffer = BytesIO()

    document = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    # Title
    story.append(
        Paragraph(
            "SUMMORA - Article Summary",
            title_style
        )
    )

    story.append(Spacer(1, 20))

    # Summary
    for line in summary.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 8))
            continue

        if line.lower().startswith("headline"):
            story.append(
                Paragraph(line, heading_style)
            )

        elif line.lower().startswith("paragraph"):
            story.append(
                Paragraph(line, heading_style)
            )

        elif line.lower().startswith("takeaways"):
            story.append(
                Paragraph(line, heading_style)
            )

        else:
            story.append(
                Paragraph(line, body_style)
            )

        story.append(Spacer(1, 6))

    # Article information
    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Article Information",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"Word Count: {word_count}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"Reading Time: {reading_time} minutes",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"Detected Topic: {topic}",
            body_style
        )
    )

    document.build(story)

    pdf_buffer.seek(0)

    return pdf_buffer.getvalue()
def build_system_prompt(
    rules: dict,
    summary_language: str = "English",
    summary_format: str = "Standard"
) -> str:
    """Build the system prompt from the JSON summarization rules."""

    accuracy_rules = "\n".join(
        f"- {rule}" for rule in rules["accuracy_rules"]
    )

    content_rules = "\n".join(
        f"- {rule}" for rule in rules["content_rules"]
    )

    headline_rules = "\n".join(
        f"- {rule}" for rule in rules["headline_rules"]
    )

    paragraph_rules = "\n".join(
        f"- {rule}" for rule in rules["paragraph_rules"]
    )

    takeaway_rules = "\n".join(
        f"- {rule}" for rule in rules["takeaway_rules"]
    )

    forbidden_behavior = "\n".join(
        f"- {rule}" for rule in rules["forbidden_behavior"]
    )

    output_format = rules["output_format"]
    
    format_instructions = {
            "Standard": """
    - Generate one concise headline.
    - Generate one paragraph containing 3 to 4 sentences.
    - Generate exactly 5 factual takeaway bullet points.
    """,

            "Short": """
    - Generate one concise headline.
    - Generate one paragraph containing exactly 2 sentences.
    - Generate exactly 3 factual takeaway bullet points.
    """,

            "Detailed": """
    - Generate one concise headline.
    - Generate one paragraph containing 5 to 6 sentences.
    - Generate exactly 7 factual takeaway bullet points.
    """
        }

    selected_format = format_instructions.get(
        summary_format,
        format_instructions["Standard"]
    )

    prompt = f"""
You are an AI News Article Summarizer.

Your task is to summarize ONLY the article provided by the user.

IMPORTANT ACCURACY RULES:
{accuracy_rules}

LANGUAGE RULE:
Generate the complete summary in {summary_language}.
The headline, paragraph, and all five takeaways must use the selected language.
Preserve the original facts, names, numbers, dates, locations, and meaning accurately.
Do not translate factual values incorrectly.

SUMMARY FORMAT:
Selected format: {summary_format}

{selected_format}

CONTENT RULES:
{content_rules}

HEADLINE RULES:
{headline_rules}

PARAGRAPH RULES:
{paragraph_rules}

TAKEAWAY RULES:
{takeaway_rules}

FORBIDDEN BEHAVIOR:
{forbidden_behavior}

REQUIRED OUTPUT FORMAT:

Headline:
Generate one concise, meaningful headline that clearly describes the main topic of the article.
The headline must NOT be empty.
Do not write only "Headline:".
Do not leave the headline blank.

Paragraph:
Follow the selected summary format above.

Takeaways:
Follow the selected summary format above.

Return exactly these three sections:
1. Headline
2. Paragraph
3. Takeaways

Do not add any information that is not present in the article.
"""

    return prompt.strip()
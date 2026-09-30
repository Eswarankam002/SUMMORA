import json
from pathlib import Path
from datetime import datetime


HISTORY_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "summary_history.json"
)


def load_history() -> list:
    """Load article history from the JSON file."""

    if not HISTORY_FILE.exists():
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_article_name(summary: str) -> str:
    """Extract the actual headline from the generated summary."""

    lines = [
        line.strip()
        for line in summary.splitlines()
        if line.strip()
    ]

    for index, line in enumerate(lines):

        # Remove Markdown formatting
        clean_line = line.replace("*", "").strip()

        # Check for Headline: or Headline
        if clean_line.lower().startswith("headline"):

            # Example:
            # **Headline:** Actual title
            if ":" in clean_line:
                headline = clean_line.split(":", 1)[1].strip()

                if headline:
                    return headline

            # Example:
            # **Headline:**
            # Thinking About Problems...
            if index + 1 < len(lines):
                next_line = lines[index + 1].strip()
                next_line = next_line.replace("*", "").strip()

                if (
                    next_line
                    and not next_line.lower().startswith("paragraph")
                    and not next_line.lower().startswith("takeaways")
                ):
                    return next_line

    return "Untitled Article"

    # Final fallback:
    # Find the first line that is not a section heading.
    for line in lines:
        if not line.lower() in {
            "headline:",
            "paragraph:",
            "takeaways:"
        }:
            return line

    return "Untitled Article"


def save_summary(
    article: str,
    summary: str
) -> None:
    """Save the original article and generated summary to history."""

    history = load_history()

    article_name = extract_article_name(summary)

    history_entry = {
        "article_name": article_name,
        "date": datetime.now().strftime("%d %B %Y"),
        "article": article,
        "summary": summary
    }

    history.append(history_entry)

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )
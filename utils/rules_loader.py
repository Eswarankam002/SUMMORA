import json
from pathlib import Path


def load_summarization_rules() -> dict:
    """Load summarization rules from the JSON configuration file."""

    rules_path = (
        Path(__file__).resolve().parent.parent
        / "config"
        / "summarization_rules.json"
    )

    with open(rules_path, "r", encoding="utf-8") as file:
        rules = json.load(file)

    return rules
import re


TOPIC_KEYWORDS = {
    "Technology": [
        "technology",
        "software",
        "hardware",
        "computer",
        "laptop",
        "smartphone",
        "artificial intelligence",
        "ai",
        "app",
        "internet",
        "cybersecurity"
    ],
    "Politics": [
        "government",
        "president",
        "minister",
        "election",
        "parliament",
        "congress",
        "political",
        "policy",
        "council"
    ],
    "Sports": [
        "football",
        "cricket",
        "basketball",
        "tennis",
        "player",
        "team",
        "match",
        "championship",
        "coach",
        "tournament"
    ],
    "Business": [
        "company",
        "business",
        "market",
        "revenue",
        "investment",
        "startup",
        "profit",
        "customer",
        "industry",
        "sales"
    ],
    "Science": [
        "research",
        "researchers",
        "scientists",
        "study",
        "laboratory",
        "experiment",
        "science",
        "discovery",
        "research institute"
    ],
    "Environment": [
        "environment",
        "climate",
        "forest",
        "mangrove",
        "pollution",
        "wildlife",
        "carbon",
        "emission",
        "ecosystem",
        "shoreline"
    ]
}


def calculate_word_count(article: str) -> int:
    """Return the number of words in the article."""

    words = article.split()
    return len(words)


def estimate_reading_time(word_count: int, words_per_minute: int = 200) -> int:
    """Estimate reading time in minutes."""

    if word_count <= 0:
        return 0

    return max(1, round(word_count / words_per_minute))


def detect_topic(article: str) -> str:
    """Detect the most likely topic category using keyword frequency."""

    article_lower = article.lower()

    topic_scores = {}

    for topic, keywords in TOPIC_KEYWORDS.items():
        score = 0

        for keyword in keywords:
            matches = re.findall(
                r"\b" + re.escape(keyword.lower()) + r"\b",
                article_lower
            )
            score += len(matches)

        topic_scores[topic] = score

    if not topic_scores or max(topic_scores.values()) == 0:
        return "Other"

    return max(topic_scores, key=topic_scores.get)


def get_article_metadata(article: str) -> dict:
    """Return all article metadata."""

    word_count = calculate_word_count(article)
    reading_time = estimate_reading_time(word_count)
    topic = detect_topic(article)

    return {
        "word_count": word_count,
        "reading_time_minutes": reading_time,
        "topic": topic
    }
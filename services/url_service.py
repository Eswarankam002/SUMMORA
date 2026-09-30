import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    """Check whether the given URL is valid."""

    try:
        parsed_url = urlparse(url)

        return parsed_url.scheme in {"http", "https"} and bool(
            parsed_url.netloc
        )

    except Exception:
        return False


def extract_article_text(url: str) -> str:
    """
    Fetch a webpage and extract readable article text.

    Returns the extracted article text.
    Raises ValueError if the URL is invalid or
    the article content cannot be extracted.
    """

    if not validate_url(url):
        raise ValueError(
            "Please enter a valid article URL."
        )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/154.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

    except requests.RequestException as error:
        raise ValueError(
            "Unable to access this URL. "
            "The website may be unavailable or blocking access."
        ) from error

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Remove elements that are usually not part
    # of the actual article content.
    for element in soup(
        [
            "script",
            "style",
            "noscript",
            "nav",
            "header",
            "footer",
            "aside",
            "form",
            "iframe"
        ]
    ):
        element.decompose()

    article = soup.find("article")

    if article:
        text = article.get_text(
            separator="\n",
            strip=True
        )
    else:
        text = soup.get_text(
            separator="\n",
            strip=True
        )

    # Clean empty lines
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    article_text = "\n\n".join(lines)

    if len(article_text) < 100:
        raise ValueError(
            "Could not extract enough article content "
            "from this URL. Please paste the article text manually."
        )

    return article_text
import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def get_groq_client():
    """Create and return a Groq API client."""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not found. "
            "Please check your .env file."
        )

    return Groq(api_key=api_key)


def generate_summary(article: str, system_prompt: str) -> str:
    """Send the article and rules to Groq and return the response."""

    client = get_groq_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": article
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
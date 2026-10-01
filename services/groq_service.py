import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            api_key = None

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not configured. "
            "Add it to .env locally or Streamlit Secrets."
        )

    return Groq(api_key=api_key)


def generate_summary(article: str, system_prompt: str) -> str:
    client = get_groq_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": article}
        ],
        temperature=0
    )

    return response.choices[0].message.content
from services.groq_service import generate_summary


article = """
NovaTech announced a new laptop called Orion.
The company said the laptop will be available from October 15, 2026.
It will cost $999 and is designed for students and professionals.
"""


system_prompt = """
You are a factual news summarization assistant.

Summarize only the information provided in the article.
Do not add external information.
Do not invent facts.
Preserve names, dates, numbers, prices, and other factual details.

Return a short factual summary.
"""


try:
    result = generate_summary(article, system_prompt)

    print("\n--- GROQ RESPONSE ---\n")
    print(result)

except Exception as error:
    print("\n--- ERROR ---\n")
    print(error)
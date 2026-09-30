from utils.rules_loader import load_summarization_rules
from utils.prompt_builder import build_system_prompt
from services.groq_service import generate_summary


article = """
NovaTech announced a new laptop called Orion on September 20, 2026.
The laptop will be available from October 15, 2026, at a price of $999.
According to the company, Orion is designed for students and professionals.
The laptop includes an AI processor and 16 GB of RAM.
"""


# Step 1: Load rules from JSON
rules = load_summarization_rules()


# Step 2: Build the system prompt
system_prompt = build_system_prompt(rules)


# Step 3: Send article + rules to Groq
result = generate_summary(article, system_prompt)


# Step 4: Display result
print("\n========== AI SUMMARY ==========\n")
print(result)
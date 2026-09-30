# SUMMORA

### Transforming Long Content into Clear Insights

SUMMORA is an AI-powered content summarization application that transforms long-form articles and web content into concise, meaningful summaries.

It helps users quickly understand the most important information without reading the entire article.

---

## 🚀 Features

- 📝 **Paste Article Content**
  - Paste long-form articles or blog content directly into the application.

- 🔗 **Article URL Summarization**
  - Enter an article URL and automatically extract readable article content.

- 🤖 **AI-Powered Summarization**
  - Generate concise summaries using the Groq API and Llama 3.3 70B.

- 🌐 **Multiple Summary Languages**
  - Generate summaries in the selected language.

- 📋 **Multiple Summary Formats**
  - Standard
  - Short
  - Detailed

- 📊 **Article Metadata**
  - Word count
  - Estimated reading time
  - Detected topic

- 📚 **Summary History**
  - Save generated summaries along with the original article.
  - Reopen previously summarized articles.

- 📄 **PDF Export**
  - Download generated summaries as PDF files.

- 📝 **TXT Export**
  - Download summaries as text files.

- 🌙 **Light / Dark Mode**
  - Switch between light and dark application themes.

- 🎯 **Accuracy-Focused Summarization**
  - Preserve important facts, names, dates, numbers, locations, and context.
  - Avoid adding information that is not present in the article.

---

## 🧠 How SUMMORA Works

```text
                    ┌─────────────────────┐
                    │     User Input      │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
            Paste Article              Article URL
                  │                         │
                  │                  Extract Article
                  │                     Content
                  └────────────┬────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Article Processing   │
                    │  + Metadata         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ JSON Summarization   │
                    │ Rules + Prompt       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Groq API       │
                    │ Llama 3.3 70B       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Generated Summary   │
                    │                     │
                    │ • Headline          │
                    │ • Paragraph         │
                    │ • Takeaways         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ History / Export    │
                    │ PDF / TXT           │
                    └─────────────────────┘
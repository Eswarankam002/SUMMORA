import streamlit as st

# --------------------------------------------------
# Theme Settings
# --------------------------------------------------

if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

from utils.metadata import get_article_metadata
from utils.rules_loader import load_summarization_rules
from utils.prompt_builder import build_system_prompt
from services.groq_service import generate_summary
from services.pdf_service import create_summary_pdf
from services.history_service import save_summary, load_history

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
# --------------------------------------------------
# Theme Icon
# --------------------------------------------------

# --------------------------------------------------
# SUMMORA Branding
# --------------------------------------------------

st.markdown(
    '<div class="main-title">SUMMORA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Transforming Long Content into Clear Insights</div>',
    unsafe_allow_html=True
)

theme_col1, theme_col2 = st.columns([8, 1])

with theme_col2:

    if st.session_state["dark_mode"]:
        theme_icon = "☀️"
        theme_help = "Switch to Light Mode"
    else:
        theme_icon = "🌙"
        theme_help = "Switch to Dark Mode"

    if st.button(
        theme_icon,
        key="theme_button",
        help=theme_help
    ):
        st.session_state["dark_mode"] = not st.session_state["dark_mode"]
        st.rerun()
    
st.set_page_config(
    
    page_title="SUMMORA | AI Content Summarizer",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    f"""
    <style>

    .main {{
        padding-top: 2rem;
    }}

    :root {{
        --bg-color: {"#0e1117" if st.session_state["dark_mode"] else "#ffffff"};
        --text-color: {"#f5f5f5" if st.session_state["dark_mode"] else "#1f2937"};
        --secondary-text: {"#b8bec9" if st.session_state["dark_mode"] else "#6b7280"};
        --card-bg: {"#161b22" if st.session_state["dark_mode"] else "#f8fafc"};
        --border-color: {"rgba(255,255,255,0.15)" if st.session_state["dark_mode"] else "rgba(128,128,128,0.25)"};
    }}

    /* Main Background */

    .stApp {{
        background-color: var(--bg-color);
        color: var(--text-color);
    }}

    /* Main Text */

    .stApp p,
    .stApp label,
    .stApp span,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4 {{
        color: var(--text-color);
    }}

    /* Title */

    .main-title {{
        text-align: center;
        font-size: 3rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
        color: var(--text-color);
    }}

    .subtitle {{
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        color: var(--secondary-text);
    }}

    /* Section Titles */

    .section-title {{
        font-size: 1.4rem;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
        color: var(--text-color);
    }}

    /* Metric Cards */

    .metric-card {{
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        background-color: var(--card-bg);
        text-align: center;
    }}

    .metric-value {{
        font-size: 1.7rem;
        font-weight: 700;
        color: var(--text-color);
    }}

    .metric-label {{
        font-size: 0.9rem;
        color: var(--secondary-text);
    }}

    /* Summary Box */

    .summary-box {{
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        background-color: var(--card-bg);
        margin-bottom: 1rem;
    }}

    /* Sidebar */

    [data-testid="stSidebar"] {{
        background-color: var(--bg-color);
    }}

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {{
        color: var(--text-color);
    }}

    /* Input Labels */

    .stTextInput label,
    .stTextArea label,
    .stSelectbox label,
    .stRadio label,
    .stFileUploader label {{
        color: var(--text-color) !important;
    }}

    /* Input Text */

    .stTextInput input,
    .stTextArea textarea {{
        color: var(--text-color) !important;
    }}

    /* Radio Buttons */

    .stRadio div[role="radiogroup"] label {{
        color: var(--text-color) !important;
    }}

    /* Selectbox */

    .stSelectbox div {{
        color: var(--text-color);
    }}

    /* Buttons */

    .stButton button {{
        color: var(--text-color) !important;
    }}

    /* Captions */

    [data-testid="stCaptionContainer"] {{
        color: var(--secondary-text) !important;
    }}

    /* Markdown */

    .stMarkdown p,
    .stMarkdown li,
    .stMarkdown strong {{
        color: var(--text-color);
    }}

    /* Theme Button */

    div[data-testid="stButton"] button {{
        border: none;
        background: transparent;
        font-size: 1.4rem;
        padding: 0.2rem 0.5rem;
    }}

    div[data-testid="stButton"] button:hover {{
        border: none;
        background: transparent;
        transform: scale(1.1);
    }}

    /* Footer */

    .footer {{
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.85rem;
        opacity: 0.6;
        color: var(--secondary-text);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    st.markdown("---")

    
    # --------------------------------------------------
    # Summary Language
    # --------------------------------------------------

    st.write("### 🌐 Summary Language")

    summary_language = st.selectbox(
        "Choose language:",
        [
            "English",
            "Telugu",
            "Hindi",
            "Tamil",
            "Kannada"
        ],
        index=0
    )
    
    # --------------------------------------------------
    # Summary Format
    # --------------------------------------------------

    st.write("### 📄 Summary Format")

    summary_format = st.selectbox(
        "Choose format:",
        [
            "Standard",
            "Short",
            "Detailed"
        ],
        index=0
    )
    
    st.markdown("---")

    st.write("### About")

    st.write(
        "SUMMORA summarizes news articles while "
        "preserving important facts, numbers, dates, "
        "names, and key information."
    )

    st.markdown("---")

    st.write("### Current Features")

    st.write("✓ AI-powered summarization")
    st.write("✓ Headline generation")
    st.write("✓ Paragraph summary")
    st.write("✓ 5 key takeaways")
    st.write("✓ Word count")
    st.write("✓ Reading time")
    st.write("✓ Topic detection")
    st.write("✓ TXT download")
    st.write("✓ PDF download")
    st.write("✓ Image upload")

    st.markdown("---")

    st.write("### 📚 Article History")

    history = load_history()

    if not history:
        st.info("No articles yet.")
    else:
        for index, item in enumerate(reversed(history), start=1):

            st.markdown(
                f"""
                **📰 {item["article_name"]}**

                📅 {item["date"]}
                """
            )

            if st.button(
                "Open",
                key=f"open_history_{index}"
            ):
                st.session_state["selected_article"] = item
                st.rerun()

# Selected Article from History
if "selected_article" in st.session_state:

    selected_article = st.session_state["selected_article"]

    st.markdown("---")
    st.subheader("📖 Opened Article")

    st.markdown(
        f"### 📰 {selected_article['article_name']}"
    )

    st.caption(
        f"📅 {selected_article['date']}"
    )

    st.markdown("### 📄 Original Article")

    st.text_area(
        "Original article",
        selected_article["article"],
        height=300,
        disabled=True,
        label_visibility="collapsed"
    )

    st.markdown("### 🤖 AI Generated Summary")

    st.markdown(
        selected_article["summary"]
    )

    if st.button("✕ Close Article"):
        del st.session_state["selected_article"]
        st.rerun()

# --------------------------------------------------
# Article Input
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📝 Article Input</div>',
    unsafe_allow_html=True
)

input_method = st.radio(
    "Choose article input method:",
    ["📝 Paste Article", "🔗 Article URL"],
    horizontal=True,
    label_visibility="collapsed"
)

if input_method == "📝 Paste Article":

    article = st.text_area(
        "Paste your article below:",
        height=300,
        placeholder=(
            "Paste a news article, blog post, or other "
            "long-form content here..."
        ),
        label_visibility="collapsed"
    )

else:

    article_url = st.text_input(
        "Article URL:",
        placeholder="https://example.com/news/article",
        label_visibility="collapsed"
    )

    if st.button("🔗 Fetch Article"):

        if not article_url.strip():

            st.warning(
                "Please enter an article URL."
            )

        else:

            from services.url_service import extract_article_text

            try:

                with st.spinner(
                    "Fetching article..."
                ):

                    article = extract_article_text(
                        article_url.strip()
                    )

                st.success(
                    "✅ Article fetched successfully!"
                )

                st.text_area(
                    "Extracted Article:",
                    article,
                    height=300,
                    disabled=True
                )

                st.session_state["url_article"] = article

            except ValueError as error:

                st.error(str(error))

                st.session_state.pop(
                    "url_article",
                    None
                )

    article = st.session_state.get(
        "url_article",
        ""
    )

# --------------------------------------------------
# Image Upload
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🖼️ Upload Article Image</div>',
    unsafe_allow_html=True
)

uploaded_image = st.file_uploader(
    "Upload an article image:",
    type=["png", "jpg", "jpeg"],
    help="Upload a screenshot or image of an article."
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Article Image",
        use_container_width=True
    )


# --------------------------------------------------
# Summarize Button
# --------------------------------------------------

summarize_button = st.button(
    "✨ Summarize Article",
    type="primary",
    use_container_width=True
)


# --------------------------------------------------
# Summarization
# --------------------------------------------------

if summarize_button:

    if not article.strip():

        st.warning(
            "Please paste an article before summarizing."
        )

    else:

        with st.spinner(
            "Analyzing and summarizing your article..."
        ):

            try:

                # --------------------------------------------------
                # Article Metadata
                # --------------------------------------------------

                metadata = get_article_metadata(article)


                # --------------------------------------------------
                # Load Summarization Rules
                # --------------------------------------------------

                rules = load_summarization_rules()


                # --------------------------------------------------
                # Build System Prompt
                # --------------------------------------------------

                system_prompt = build_system_prompt(
                    rules,
                    summary_language,
                    summary_format
                )


                # --------------------------------------------------
                # Generate AI Summary
                # --------------------------------------------------

                summary = generate_summary(
                    article,
                    system_prompt
                )
                
                save_summary(
                    article=article,
                    summary=summary
                )


                # --------------------------------------------------
                # Article Information
                # --------------------------------------------------

                st.markdown(
                    '<div class="section-title">'
                    '📊 Article Information'
                    '</div>',
                    unsafe_allow_html=True
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-value">
                                {metadata["word_count"]}
                            </div>
                            <div class="metric-label">
                                Words
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-value">
                                {metadata["reading_time_minutes"]} min
                            </div>
                            <div class="metric-label">
                                Reading Time
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col3:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-value">
                                {metadata["topic"]}
                            </div>
                            <div class="metric-label">
                                Detected Topic
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                # --------------------------------------------------
                # AI Summary
                # --------------------------------------------------

                st.markdown(
                    '<div class="section-title">'
                    '🤖 AI Summary'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="summary-box">
                        {summary.replace(chr(10), "<br>")}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # --------------------------------------------------
                # Download Summary
                # --------------------------------------------------

                st.markdown(
                    '<div class="section-title">'
                    '📥 Download Summary'
                    '</div>',
                    unsafe_allow_html=True
                )

                download_content = f"""SUMMORA - Article Summary

{summary}

----------------------------------------
Article Information
----------------------------------------

Word Count: {metadata["word_count"]}
Reading Time: {metadata["reading_time_minutes"]} minutes
Detected Topic: {metadata["topic"]}
"""

                st.download_button(
                    label="📄 Download TXT",
                    data=download_content,
                    file_name="summora_summary.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                pdf_data = create_summary_pdf(
                    summary=summary,
                    word_count=metadata["word_count"],
                    reading_time=metadata["reading_time_minutes"],
                    topic=metadata["topic"]
)

                st.download_button(
                    label="📕 Download PDF",
                    data=pdf_data,
                    file_name="summora_summary.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

            except Exception as error:

                st.error(
                    "Something went wrong while generating "
                    f"the summary: {error}"
                )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        SUMMORA • AI-Powered Content Summarization
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="🌍 Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

# ================= TITLE =================
st.title("🌍 AI Language Translation Tool")
st.markdown("Translate text instantly between multiple languages.")

st.divider()

# ================= INPUT =================
text = st.text_area(
    "Enter text to translate",
    height=180,
    placeholder="Type something here..."
)

st.caption(f"Characters: {len(text)}")

st.divider()

# ================= LANGUAGES =================
languages = [
    "English",
    "Hindi",
    "French",
    "German",
    "Spanish",
    "Japanese",
    "Chinese",
    "Korean",
    "Arabic"
]

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        languages
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        languages,
        index=1
    )

st.divider()

translate_btn = st.button(
    "🌍 Translate",
    use_container_width=True
)

if translate_btn:

    if text.strip() == "":
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.warning("Source and Target languages cannot be the same.")

    else:

        language_codes = {
            "English": "en",
            "Hindi": "hi",
            "French": "fr",
            "German": "de",
            "Spanish": "es",
            "Japanese": "ja",
            "Chinese": "zh-CN",
            "Korean": "ko",
            "Arabic": "ar"
        }

        try:
            with st.spinner("Translating... Please wait..."):
                translated = GoogleTranslator(
                    source=language_codes[source_language],
                    target=language_codes[target_language]
                ).translate(text)

            st.subheader("🌍 Translated Text")

            st.text_area(
                "Result",
                translated,
                height=180
            )

            if st.button("📋 Copy Translation"):
                pyperclip.copy(translated)
                st.success("Translation copied successfully!")

            st.download_button(
                label="📥 Download Translation",
                data=translated,
                file_name="translated_text.txt",
                mime="text/plain"
            )

        except Exception:
            st.error("Translation failed. Please check your internet connection and try again.")

st.divider()
st.caption("Developed by Muskan Gupta | CodeAlpha AI Internship")
"""Optional Google Gemini-powered chat page for TimeCraft."""

import os

import streamlit as st
from duckduckgo_search import DDGS
from google import genai


st.set_page_config(page_title="TimeCraft | AI Assistant", page_icon="✨", layout="centered")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-flash-latest")


def get_api_key() -> str:
    """Read the Gemini key from the environment or Streamlit Secrets."""
    key = os.getenv("GOOGLE_API_KEY", "").strip()
    if key:
        return key
    try:
        return str(st.secrets.get("GOOGLE_API_KEY", "")).strip()
    except Exception:
        return ""


api_key = get_api_key()
client = None
if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except Exception:
        st.error("Gemini could not be initialized. Check the API key and model configuration.")
else:
    st.info(
        "The AI assistant is optional. Set GOOGLE_API_KEY in your environment or Streamlit Secrets "
        "to enable it. The other TimeCraft pages work without an API key."
    )

st.title("🎓 TimeCraft AI Assistant")
st.caption("Ask a history question. Include the word “images” to search for related pictures.")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.caption(f"Model: `{MODEL_NAME}`")
    if st.button("Clear conversation", width="stretch"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        for image_url in message.get("images", []):
            st.image(image_url, width="stretch")

prompt = st.chat_input("What would you like to explore?", disabled=client is None)

if prompt and client is not None:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response_parts = []
            with st.spinner("Thinking..."):
                for chunk in client.models.generate_content_stream(
                    model=MODEL_NAME,
                    contents=prompt,
                ):
                    text = getattr(chunk, "text", "") or ""
                    if text:
                        response_parts.append(text)
                        response_placeholder.markdown("".join(response_parts) + "▌")

            full_response = "".join(response_parts).strip()
            if not full_response:
                full_response = "The model returned no text. Please try rephrasing your question."
            response_placeholder.markdown(full_response)

            found_images = []
            image_terms = ("image", "images", "picture", "pictures", "show me")
            if any(term in prompt.casefold() for term in image_terms):
                clean_query = prompt
                for term in image_terms:
                    clean_query = clean_query.replace(term, "")
                try:
                    with st.status("Searching for images...", expanded=False) as status:
                        with DDGS() as search:
                            results = list(search.images(clean_query.strip(), max_results=3))
                        found_images = [item["image"] for item in results if item.get("image")]
                        if found_images:
                            image_columns = st.columns(len(found_images))
                            for column, image_url in zip(image_columns, found_images):
                                column.image(image_url, width="stretch")
                            status.update(label="Image search complete", state="complete")
                        else:
                            status.update(label="No matching images found", state="complete")
                except Exception:
                    st.warning("Image search is unavailable right now. You can continue the text conversation.")

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response, "images": found_images}
        )
    except Exception as error:
        st.error("Gemini could not return a response. Check the key and your internet connection, then try again.")
        with st.expander("Technical details"):
            st.code(str(error))

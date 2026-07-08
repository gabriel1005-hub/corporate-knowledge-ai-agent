import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.services.query_service import QueryService

# ------------------------------------------------------
# Config
# ------------------------------------------------------

st.set_page_config(
    page_title="NovaCore Knowledge AI",
    page_icon="🧠",
    layout="wide",
)

# ------------------------------------------------------
# Sidebar
# ------------------------------------------------------

with st.sidebar:

    st.title("🧠 NovaCore")

    st.markdown("---")

    st.subheader("System Status")

    st.success("Ollama Connected")

    st.success("ChromaDB Ready")

    st.success("Knowledge Base Loaded")

    st.markdown("---")

    st.subheader("Models")

    st.write("Embedding")
    st.code("nomic-embed-text")

    st.write("LLM")
    st.code("qwen2.5:3b")

    st.markdown("---")

    st.caption("NovaCore Knowledge AI")

# ------------------------------------------------------
# Main
# ------------------------------------------------------

st.title("🧠 NovaCore Knowledge AI")

st.caption(
    "Enterprise Knowledge Assistant powered by Local AI"
)

service = QueryService()

question = st.text_input(
    "Ask anything about your company documentation"
)

if st.button("Ask"):

    if question:

        with st.spinner("Searching..."):

            answer = service.ask(question)

        st.markdown("## Answer")

        st.write(answer)
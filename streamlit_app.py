import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.services.query_service import QueryService
from app.services.system_service import SystemService


# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="NovaCore Knowledge AI",
    page_icon="🧠",
    layout="wide",
)

# -------------------------------------------------------
# SERVICES
# -------------------------------------------------------

@st.cache_resource
def get_query_service():
    return QueryService()


@st.cache_resource
def get_system_service():
    return SystemService()


query_service = get_query_service()
system_service = get_system_service()

stats = system_service.get_stats()

# -------------------------------------------------------
# SESSION
# -------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "answer": (
                "👋 Welcome to **NovaCore Knowledge AI**.\n\n"
                "I'm your enterprise knowledge assistant.\n\n"
                "Ask me anything about the company documentation."
            ),
            "sources": [],
        }
    ]

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

with st.sidebar:

    st.title("🧠 NovaCore")

    st.caption("Enterprise Knowledge Assistant")

    st.divider()

    st.subheader("System Status")

    st.success("🟢 Ollama Connected")
    st.success("🟢 ChromaDB Ready")
    st.success("🟢 Knowledge Base Loaded")

    st.divider()

    st.subheader("Knowledge Base")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Documents", stats["documents"])

    with col2:
        st.metric("Chunks", stats["chunks"])

    st.divider()

    st.subheader("Models")

    st.write("Embedding")

    st.code(stats["embedding_model"])

    st.write("LLM")

    st.code(stats["llm_model"])

    st.divider()

    st.caption("Powered by Ollama + ChromaDB")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.title("🧠 NovaCore Knowledge AI")

st.caption(
    "Enterprise Knowledge Assistant powered by Local AI"
)

# -------------------------------------------------------
# CHAT HISTORY
# -------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["answer"])

        if message["sources"]:

            st.markdown("#### 📚 Sources")

            for source in message["sources"]:

                with st.container(border=True):

                    st.write(f"📄 {source}")

# -------------------------------------------------------
# CHAT INPUT
# -------------------------------------------------------

prompt = st.chat_input(
    "Ask something about your company..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "answer": prompt,
            "sources": [],
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        start = time.perf_counter()

        with st.spinner("Searching corporate knowledge..."):

            response = query_service.ask(prompt)

        elapsed = time.perf_counter() - start

        st.markdown(response["answer"])

        if response["sources"]:

            st.markdown("#### 📚 Sources")

            for source in response["sources"]:

                with st.container(border=True):

                    st.write(f"📄 {source}")

        st.caption(f"⏱ Response time: {elapsed:.2f} seconds")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "answer": response["answer"],
            "sources": response["sources"],
        }
    )
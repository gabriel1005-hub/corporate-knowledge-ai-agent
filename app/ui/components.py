"""
Reusable Streamlit UI components.
"""

import streamlit as st


def render_header():

    st.title("🧠 NovaCore Knowledge AI")

    st.caption(
        "Enterprise Knowledge Assistant powered by Local AI"
    )


def render_sidebar(stats):

    with st.sidebar:

        st.title("🧠 NovaCore")

        st.caption(
            "Enterprise Knowledge Assistant"
        )

        st.divider()

        st.subheader("System Status")

        st.success("🟢 Ollama Connected")

        st.success("🟢 ChromaDB Ready")

        st.success("🟢 Knowledge Base Loaded")

        st.divider()

        st.subheader("Knowledge Base")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Documents",
                stats["documents"],
            )

        with col2:

            st.metric(
                "Chunks",
                stats["chunks"],
            )

        st.divider()

        st.subheader("Models")

        st.write("Embedding")

        st.code(
            stats["embedding_model"]
        )

        st.write("LLM")

        st.code(
            stats["llm_model"]
        )

        st.divider()

        st.caption(
            "Powered by Ollama + ChromaDB"
        )


def render_sources(sources):

    if not sources:

        return

    st.markdown("### 📚 Sources")

    for source in sources:

        with st.container(border=True):

            st.write(f"📄 {source}")


def render_footer():

    st.divider()

    st.caption(
        "NovaCore Knowledge AI • 2026"
    )
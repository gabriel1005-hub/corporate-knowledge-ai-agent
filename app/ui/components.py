"""
Reusable UI components.
"""

from collections import defaultdict

import streamlit as st

from app.ui.kit.source_cards import source_card


# ==========================================================
# HEADER
# ==========================================================

def render_header():

    left, right = st.columns([6, 1])

    with left:

        st.title("🧠 NovaCore")

        st.caption(
            "Enterprise Knowledge AI"
        )

    with right:

        st.markdown(
            """
<div style="
margin-top:18px;
padding:10px;
background:#22C55E;
color:white;
font-weight:600;
text-align:center;
border-radius:12px;
">
🟢 Local AI
</div>
""",
            unsafe_allow_html=True,
        )

    st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar(stats):

    with st.sidebar:

        st.title("🧠 NovaCore")

        st.caption(
            "Enterprise Knowledge AI"
        )

        st.divider()

        with st.expander(
            "🟢 System",
            expanded=True,
        ):

            st.success(
                "Ollama Connected"
            )

            st.success(
                "Chroma Ready"
            )

            st.success(
                "Knowledge Base Loaded"
            )

        with st.expander(
            "🧠 Models"
        ):

            st.write("Embedding")

            st.code(
                stats["embedding_model"]
            )

            st.write("LLM")

            st.code(
                stats["llm_model"]
            )


# ==========================================================
# SOURCES
# ==========================================================

def render_sources(sources):

    if not sources:

        return

    grouped = defaultdict(list)

    for source in sources:

        grouped[
            source["document"]
        ].append(
            source["chunk"]
        )

    st.markdown(
        "### 📚 Sources"
    )

    for document, chunks in grouped.items():

        source_card(
            document=document,
            chunks=chunks,
        )


# ==========================================================
# FOOTER
# ==========================================================

def render_footer():

    st.divider()

    st.caption(
        "NovaCore Knowledge AI • 2026"
    )
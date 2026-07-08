import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.services.query_service import QueryService
from app.services.system_service import SystemService

from app.ui.components import (
    render_header,
    render_sidebar,
    render_sources,
    render_footer,
)

from app.ui.styles import load_css


st.set_page_config(
    page_title="NovaCore Knowledge AI",
    page_icon="🧠",
    layout="wide",
)

load_css()


@st.cache_resource
def get_query_service():
    return QueryService()


@st.cache_resource
def get_system_service():
    return SystemService()


query_service = get_query_service()
system_service = get_system_service()

stats = system_service.get_stats()


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


render_sidebar(stats)

render_header()


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["answer"])

        render_sources(
            message["sources"]
        )


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

        with st.spinner(
            "Searching corporate knowledge..."
        ):

            response = query_service.ask(
                prompt
            )

        elapsed = time.perf_counter() - start

        st.markdown(
            response["answer"]
        )

        render_sources(
            response["sources"]
        )

        st.caption(
            f"⏱ Response time: {elapsed:.2f} seconds"
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "answer": response["answer"],
            "sources": response["sources"],
        }
    )


render_footer()
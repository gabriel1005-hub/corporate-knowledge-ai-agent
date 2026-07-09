"""
Chat UI.
"""

import time

import streamlit as st

from app.ui.components import render_sources
from app.ui.kit.hero import render_hero
from app.ui.kit.messages import (
    assistant_message,
    user_message,
)


def render_chat(
    query_service,
    analytics_service,
):
    """
    Render chat interface.
    """

    # -------------------------------------------------
    # Session
    # -------------------------------------------------

    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "answer": (
                    "Welcome to NovaCore Knowledge AI.\n\n"
                    "I'm your enterprise knowledge assistant.\n\n"
                    "Ask me anything about your corporate documentation."
                ),
                "sources": [],
            }
        ]

    # -------------------------------------------------
    # Hero
    # -------------------------------------------------

    if len(st.session_state.messages) == 1:

        render_hero()

    # -------------------------------------------------
    # History
    # -------------------------------------------------

    for message in st.session_state.messages:

        if message["role"] == "assistant":

            assistant_message(
                message["answer"]
            )

            render_sources(
                message["sources"]
            )

        else:

            user_message(
                message["answer"]
            )

    # -------------------------------------------------
    # Input
    # -------------------------------------------------

    prompt = st.chat_input(
        "Ask something about your company..."
    )

    if not prompt:
        return

    # -------------------------------------------------
    # Save user
    # -------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "answer": prompt,
            "sources": [],
        }
    )

    # -------------------------------------------------
    # Generate answer
    # -------------------------------------------------

    start = time.perf_counter()

    with st.spinner(
        "Searching corporate knowledge..."
    ):

        response = query_service.ask(
            prompt
        )

    elapsed = (
        time.perf_counter() - start
    )

    analytics_service.register_query(
        question=prompt,
        response_time=elapsed,
        sources=response["sources"],
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "answer": response["answer"],
            "sources": response["sources"],
        }
    )

    st.rerun()
"""
Load NovaCore Design System.
"""

from pathlib import Path

import streamlit as st


CSS_FILES = [
    "variables.css",
    "reset.css",
    "layout.css",
    "sidebar.css",
    "tabs.css",
    "cards.css",
    "buttons.css",
    "chat.css",
    "tables.css",
    "forms.css",
    "animations.css",
    "utilities.css",
]


def load_css():
    """
    Load every CSS module.
    """

    theme_dir = (
        Path(__file__).parent
        / "theme"
    )

    css = ""

    for file in CSS_FILES:

        css += (
            theme_dir / file
        ).read_text(
            encoding="utf-8"
        )

        css += "\n"

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )
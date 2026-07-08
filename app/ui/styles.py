"""
Custom CSS styles for NovaCore Knowledge AI.
"""

import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1200px;
        }

        section[data-testid="stSidebar"]{
            border-right:1px solid rgba(255,255,255,.08);
        }

        div[data-testid="stMetric"]{
            background:#1f1f27;
            padding:12px;
            border-radius:12px;
        }

        div[data-testid="stChatMessage"]{
            border-radius:16px;
        }

        code{
            border-radius:8px !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
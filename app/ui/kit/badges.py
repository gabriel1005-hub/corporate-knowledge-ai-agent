"""
NovaCore UI Badges.
"""

import streamlit as st


def status_badge(
    text: str,
    color: str = "success",
):
    """
    Enterprise badge.
    """

    colors = {
        "success": "#22C55E",
        "warning": "#F59E0B",
        "danger": "#EF4444",
        "primary": "#2563EB",
        "neutral": "#64748B",
    }

    background = colors.get(
        color,
        colors["primary"],
    )

    st.markdown(
        f"""
<div
class="nova-badge"
style="background:{background};">
{text}
</div>
""",
        unsafe_allow_html=True,
    )
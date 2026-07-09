"""
NovaCore Enterprise Cards.
"""

import streamlit as st


def stat_card(
    title: str,
    value,
    icon: str,
    subtitle: str = "",
):

    st.markdown(
        f"""
<div class="nova-stat-card">

<div class="nova-stat-icon">
{icon}
</div>

<div class="nova-stat-value">
{value}
</div>

<div class="nova-stat-title">
{title}
</div>

<div class="nova-stat-subtitle">
{subtitle}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


def info_card(
    title,
    subtitle,
    footer="",
):

    st.markdown(
        f"""
<div class="nova-info-card">

<div class="nova-info-title">
{title}
</div>

<div class="nova-info-subtitle">
{subtitle}
</div>

<div class="nova-info-footer">
{footer}
</div>

</div>
""",
        unsafe_allow_html=True,
    )
"""
NovaCore Hero Component.
"""

import streamlit as st


def render_hero():
    """
    Hero section shown before the first question.
    """

    st.markdown(
        """
<div class="nova-hero">

<div class="nova-hero-logo">
🧠
</div>

<h1>NovaCore</h1>

<p>
Enterprise Knowledge AI powered by Local LLMs
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
            "📚 Search corporate documentation"
        )

    with c2:

        st.info(
            "⚡ Instant semantic retrieval"
        )

    with c3:

        st.info(
            "🔒 100% Local AI"
        )
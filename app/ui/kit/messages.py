"""
NovaCore Message Cards.
"""

import streamlit as st


def assistant_message(
    answer: str,
    response_time: float | None = None,
):
    """
    Assistant message card.
    """

    st.markdown(
        f"""
<div class="nova-message">

<div class="nova-message-header">
🤖 NovaCore
</div>

<div class="nova-message-content">

{answer}

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    if response_time is not None:

        st.caption(
            f"⚡ Response time: {response_time:.2f} sec"
        )


def user_message(
    question: str,
):
    """
    User message.
    """

    st.markdown(
        f"""
<div class="nova-user">

👤 {question}

</div>
""",
        unsafe_allow_html=True,
    )
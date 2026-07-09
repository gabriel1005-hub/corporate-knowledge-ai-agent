"""
NovaCore Source Cards.
"""

import streamlit as st


def source_card(
    document: str,
    chunks: list[int],
):
    """
    Render one source card.
    """

    chunk_text = " • ".join(
        f"#{c}"
        for c in sorted(chunks)
    )

    st.markdown(
        f"""
<div class="nova-source-card">

<div class="nova-source-title">

📄 {document}

</div>

<div class="nova-source-chunks">

🧩 Chunks

{chunk_text}

</div>

</div>
""",
        unsafe_allow_html=True,
    )
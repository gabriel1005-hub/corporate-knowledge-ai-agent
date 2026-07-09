"""
Reusable Plotly charts.
"""

import plotly.express as px
import streamlit as st


# ==========================================================
# QUERIES PER DAY
# ==========================================================

def render_queries_chart(df):
    """
    Queries per day.
    """

    if df.empty:

        st.info(
            "No query history available."
        )

        return

    fig = px.line(
        df,
        x="date",
        y="queries",
        markers=True,
        title="Queries per Day",
    )

    fig.update_layout(
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),
        height=350,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# ==========================================================
# RESPONSE TIME
# ==========================================================

def render_response_time_chart(df):
    """
    Average response time.
    """

    if df.empty:

        st.info(
            "No response time data."
        )

        return

    fig = px.line(
        df,
        x="date",
        y="response_time",
        markers=True,
        title="Average Response Time",
    )

    fig.update_layout(
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),
        height=350,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# ==========================================================
# DOCUMENTS
# ==========================================================

def render_documents_chart(ranking):
    """
    Most consulted documents.
    """

    if not ranking:

        st.info(
            "No document statistics available."
        )

        return

    documents = [
        item[0]
        for item in ranking
    ]

    counts = [
        item[1]
        for item in ranking
    ]

    fig = px.bar(
        x=counts,
        y=documents,
        orientation="h",
        title="Most Consulted Documents",
    )

    fig.update_layout(
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),
        height=350,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
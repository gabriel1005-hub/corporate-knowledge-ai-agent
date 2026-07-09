"""
Analytics dashboard.
"""

import streamlit as st

from app.ui.charts import (
    render_documents_chart,
    render_queries_chart,
    render_response_time_chart,
)
from app.ui.kit.cards import stat_card


def render_analytics(
    analytics_service,
    stats,
):
    """
    Render analytics dashboard.
    """

    st.header("📊 Analytics Dashboard")

    st.caption(
        "Insights about NovaCore Knowledge AI usage."
    )

    total_queries = analytics_service.total_queries()

    avg_response = (
        analytics_service.average_response_time()
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        stat_card(
            "Questions",
            total_queries,
            "💬",
        )

    with c2:
        stat_card(
            "Avg Response",
            f"{avg_response:.2f}s",
            "⚡",
        )

    with c3:
        stat_card(
            "Documents",
            stats["documents"],
            "📄",
        )

    with c4:
        stat_card(
            "Chunks",
            stats["chunks"],
            "🧩",
        )

    st.divider()

    render_queries_chart(
        analytics_service.queries_per_day()
    )

    st.divider()

    render_response_time_chart(
        analytics_service.response_time_history()
    )

    st.divider()

    render_documents_chart(
        analytics_service.most_consulted_documents()
    )

    st.divider()

    st.subheader("🕒 Latest Questions")

    latest = analytics_service.latest_queries()

    if not latest:

        st.info(
            "No questions have been registered."
        )

        return

    for item in latest:

        with st.container(border=True):

            st.write(
                item["question"]
            )

            st.caption(
                f"⏱ {item['response_time']} seconds"
            )
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.services.analytics_service import AnalyticsService
from app.services.indexing_service import IndexingService
from app.services.query_service import QueryService
from app.services.system_service import SystemService

from app.ui.analytics import render_analytics
from app.ui.chat import render_chat
from app.ui.components import (
    render_footer,
    render_header,
    render_sidebar,
)
from app.ui.documents import render_documents
from app.ui.styles import load_css


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="NovaCore Knowledge AI",
    page_icon="🧠",
    layout="wide",
)

load_css()


# ==========================================================
# SERVICES
# ==========================================================

@st.cache_resource
def get_query_service():
    return QueryService()


@st.cache_resource
def get_system_service():
    return SystemService()


@st.cache_resource
def get_indexing_service():
    return IndexingService()


@st.cache_resource
def get_analytics_service():
    return AnalyticsService()


query_service = get_query_service()
system_service = get_system_service()
indexing_service = get_indexing_service()
analytics_service = get_analytics_service()

stats = system_service.get_stats()


# ==========================================================
# LAYOUT
# ==========================================================

render_sidebar(stats)

render_header()

tab_chat, tab_analytics, tab_documents, tab_settings = st.tabs(
    [
        "💬 Chat",
        "📊 Analytics",
        "📚 Documents",
        "⚙ Settings",
    ]
)


# ==========================================================
# CHAT
# ==========================================================

with tab_chat:

    render_chat(
        query_service=query_service,
        analytics_service=analytics_service,
    )


# ==========================================================
# ANALYTICS
# ==========================================================

with tab_analytics:

    render_analytics(
        analytics_service=analytics_service,
        stats=stats,
    )


# ==========================================================
# DOCUMENTS
# ==========================================================

with tab_documents:

    render_documents(
        indexing_service=indexing_service,
    )


# ==========================================================
# SETTINGS
# ==========================================================

with tab_settings:

    st.subheader("⚙ Settings")

    st.info(
        "Settings panel coming soon."
    )


# ==========================================================
# FOOTER
# ==========================================================

render_footer()
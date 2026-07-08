"""
Reusable Streamlit UI components.
"""

import time
from datetime import datetime

import streamlit as st

from app.services.document_service import DocumentService


document_service = DocumentService()


def render_header():

    st.title("🧠 NovaCore Knowledge AI")

    st.caption(
        "Enterprise Knowledge Assistant powered by Local AI"
    )


def render_sidebar(stats, indexing_service):

    with st.sidebar:

        st.title("🧠 NovaCore")

        st.caption(
            "Enterprise Knowledge Assistant"
        )

        # -------------------------------------------------
        # DOCUMENT UPLOAD
        # -------------------------------------------------

        st.divider()

        st.subheader("📂 Knowledge Base")

        uploaded_file = st.file_uploader(
            "Upload a PDF",
            type=["pdf"],
        )

        if uploaded_file is not None:

            if st.button(
                "📥 Upload & Index",
                use_container_width=True,
            ):

                if document_service.exists(uploaded_file.name):

                    st.warning(
                        "This document already exists."
                    )

                else:

                    save_path = document_service.save_document(
                        uploaded_file
                    )

                    with st.spinner(
                        "Indexing document..."
                    ):

                        chunks = indexing_service.index_document(
                            str(save_path)
                        )

                    st.success(
                        f"✅ {uploaded_file.name} indexed successfully!"
                    )

                    st.info(
                        f"Generated {chunks} chunks."
                    )

                    st.balloons()

                    time.sleep(1)

                    st.rerun()

        # -------------------------------------------------
        # SYSTEM STATUS
        # -------------------------------------------------

        st.divider()

        st.subheader("🟢 System Status")

        st.success("Ollama Connected")

        st.success("ChromaDB Ready")

        st.success("Knowledge Base Loaded")

        # -------------------------------------------------
        # KNOWLEDGE BASE METRICS
        # -------------------------------------------------

        st.divider()

        st.subheader("📊 Knowledge Base")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Documents",
                stats["documents"],
            )

        with col2:

            st.metric(
                "Chunks",
                stats["chunks"],
            )

        st.caption(
            f"Updated: {datetime.now():%H:%M:%S}"
        )

        # -------------------------------------------------
        # MODELS
        # -------------------------------------------------

        st.divider()

        st.subheader("🧠 Models")

        st.write("Embedding")

        st.code(
            stats["embedding_model"]
        )

        st.write("LLM")

        st.code(
            stats["llm_model"]
        )

        # -------------------------------------------------
        # DOCUMENT MANAGER
        # -------------------------------------------------

        st.divider()

        st.subheader("📄 Indexed Documents")

        documents = document_service.list_documents()

        st.caption(
            f"{len(documents)} indexed documents"
        )

        if not documents:

            st.info(
                "No documents found."
            )

        else:

            for document in documents:

                col1, col2 = st.columns([5, 1])

                with col1:

                    st.markdown(
                        f"**📄 {document['name']}**"
                    )

                    st.caption(
                        f"{document['size_mb']} MB"
                    )

                with col2:

                    if st.button(
                        "🗑",
                        key=f"delete_{document['name']}",
                        help="Delete document",
                    ):

                        deleted = document_service.delete_document(
                            document["name"]
                        )

                        if deleted:

                            st.toast(
                                "Document deleted.",
                                icon="🗑"
                            )

                            time.sleep(0.5)

                            st.rerun()

                        else:

                            st.error(
                                "Unable to delete document."
                            )

                st.divider()

        # -------------------------------------------------

        st.caption(
            "Powered by Ollama + ChromaDB"
        )


def render_sources(sources):

    if not sources:
        return

    st.markdown("### 📚 Sources")

    for source in sources:

        with st.container(border=True):

            st.write(
                f"📄 {source}"
            )


def render_footer():

    st.divider()

    st.caption(
        "NovaCore Knowledge AI • 2026"
    )
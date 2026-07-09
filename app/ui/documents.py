"""
Documents UI.
"""

import time

import streamlit as st

from app.services.document_service import DocumentService

document_service = DocumentService()


def render_documents(
    indexing_service,
):
    """
    Documents page.
    """

    st.header("📚 Documents")

    st.caption(
        "Manage your corporate knowledge base."
    )

    st.divider()

    # -------------------------------------------------
    # Upload
    # -------------------------------------------------

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
    )

    if uploaded_file is not None:

        if st.button(
            "📥 Upload & Index",
            use_container_width=True,
        ):

            if document_service.exists(
                uploaded_file.name
            ):

                st.warning(
                    "Document already exists."
                )

            else:

                save_path = (
                    document_service.save_document(
                        uploaded_file
                    )
                )

                with st.spinner(
                    "Indexing..."
                ):

                    chunks = (
                        indexing_service.index_document(
                            str(save_path)
                        )
                    )

                st.success(
                    f"{chunks} chunks generated."
                )

                time.sleep(1)

                st.rerun()

    st.divider()

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    search = st.text_input(
        "🔎 Search document...",
        placeholder="Employee Handbook",
    )

    documents = (
        document_service.list_documents()
    )

    if search:

        search = search.lower()

        documents = [

            doc

            for doc in documents

            if search in doc[
                "name"
            ].lower()

        ]

    st.subheader(
        f"Documents ({len(documents)})"
    )

    if not documents:

        st.info(
            "No matching documents."
        )

        return

    # -------------------------------------------------
    # Documents
    # -------------------------------------------------

    for document in documents:

        col1, col2 = st.columns(
            [6, 1]
        )

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
                key=document["name"],
            ):

                deleted = (
                    document_service.delete_document(
                        document["name"]
                    )
                )

                if deleted:

                    st.toast(
                        "Deleted",
                        icon="🗑"
                    )

                    time.sleep(.5)

                    st.rerun()

        st.divider()
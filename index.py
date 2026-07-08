from app.services.indexing_service import IndexingService


def main():

    print("=" * 60)
    print("NovaCore Document Indexer")
    print("=" * 60)

    service = IndexingService()

    service.index_documents()

    print("\n✅ Index created successfully!")


if __name__ == "__main__":
    main()
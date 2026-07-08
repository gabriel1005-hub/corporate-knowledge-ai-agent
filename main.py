from app.services.indexing_service import IndexingService


def main():

    service = IndexingService()

    service.index_documents()


if __name__ == "__main__":
    main()
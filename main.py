from app.models.document import Document


def main():
    document = Document(
        content="Welcome to NovaCore Analytics",
        source="onboarding.pdf",
        file_type="pdf",
        metadata={
            "pages": 12,
            "department": "HR"
        }
    )

    print(document)


if __name__ == "__main__":
    main()
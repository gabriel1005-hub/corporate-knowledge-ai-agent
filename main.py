from app.services.query_service import QueryService


def main():

    service = QueryService()

    print("=" * 60)
    print("NovaCore Knowledge AI")
    print("=" * 60)

    while True:

        question = input("\nQuestion: ")

        if question.lower() in {"exit", "quit"}:
            break

        answer = service.ask(question)

        print("\n" + "=" * 60)
        print(answer)
        print("=" * 60)


if __name__ == "__main__":
    main()
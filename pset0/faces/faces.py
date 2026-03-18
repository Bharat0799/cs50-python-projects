def convert(text: str) -> str:
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main() -> None:
    user_input = input("Text: ")
    print(convert(user_input))


if __name__ == "__main__":
    main()

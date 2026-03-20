"""Simple CLI calculator supporting basic arithmetic operations."""

from typing import Callable, Dict, Tuple

Operation = Tuple[str, Callable[[float, float], float]]

OPERATIONS: Dict[str, Operation] = {
    "1": ("Addition", lambda a, b: a + b),
    "2": ("Subtraction", lambda a, b: a - b),
    "3": ("Multiplication", lambda a, b: a * b),
    "4": ("Division", lambda a, b: a / b),
}


def prompt_numbers() -> Tuple[float, float]:
    """Collect two numeric inputs from the user with validation."""
    while True:
        try:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            return first, second
        except ValueError:
            print("Please enter valid numbers.\n")


def calculate(choice: str) -> None:
    """Perform the selected operation and display the result."""
    first, second = prompt_numbers()
    label, func = OPERATIONS[choice]
    try:
        result = func(first, second)
    except ZeroDivisionError:
        print("Cannot divide by zero.\n")
        return

    print(f"Result of {label.lower()}: {result}\n")


def main() -> None:
    print("CLI Calculator\n----------------")
    while True:
        print("Choose an operation:")
        for key, (name, _) in OPERATIONS.items():
            print(f" {key}. {name}")
        print(" q. Quit")

        choice = input("Selection: ").strip().lower()
        if choice in {"q", "quit"}:
            print("Goodbye!")
            break
        if choice not in OPERATIONS:
            print("Select a valid option.\n")
            continue

        calculate(choice)


if __name__ == "__main__":
    main()

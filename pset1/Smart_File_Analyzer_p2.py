print("Welcome to Smart CLI Tool 🚀")

choice = input("Choose (file/math/greet): ").lower()

if choice == "file":
    file = input("Enter file name: ").lower()
    if file.endswith(".jpg"):
        print("Image File")
    elif file.endswith(".pdf"):
        print("PDF File")
    else:
        print("Unknown File")

elif choice == "math":
    exp = input("Enter expression: ")
    x, op, y = exp.split()
    x = float(x)
    y = float(y)

    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)

elif choice == "greet":
    g = input("Greeting: ").lower()
    if g.startswith("hello"):
        print("Free Entry")
    else:
        print("Paid Entry")
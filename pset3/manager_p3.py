menu = {
    "Pizza": 120,
    "Burger": 80,
    "Coke": 40,
    "Fries": 60
}

cart = {}
total = 0

def show_menu():
    print("\n🍔 MENU:")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def add_item():
    global total
    item = input("Enter item: ").title()

    if item in menu:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1

        total += menu[item]
        print(f"✅ Added {item}")
    else:
        print("❌ Item not available")

def show_cart():
    print("\n🛒 CART:")
    for item in sorted(cart):
        print(f"{cart[item]} x {item}")
    print(f"💰 Total: ₹{total}")

def fuel_like_discount():
    try:
        fraction = input("Enter discount fraction (x/y): ")
        x, y = fraction.split("/")
        x, y = int(x), int(y)

        if y == 0 or x > y:
            print("Invalid fraction")
            return 0

        percent = round((x / y) * 100)

        print(f"🎯 Discount: {percent}%")
        return percent

    except:
        print("Invalid input")
        return 0

def checkout():
    discount = fuel_like_discount()
    final = total - (total * discount / 100)
    print(f"\n🧾 Final Bill: ₹{round(final, 2)}")

# MAIN LOOP
while True:
    print("\n1. Show Menu")
    print("2. Add Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_item()
    elif choice == "3":
        show_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("👋 Thank you!")
        break
    else:
        print("Invalid choice")
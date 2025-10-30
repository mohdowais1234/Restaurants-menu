
menu = {
    'pizza': 140,
    'pasta': 90,
    'burger': 80,
    'coffee': 60,
    'momos': 70,
    'french fries': 89,
    'Chawmin': 80,
    'Dosa': 120,
    'Roasted': 79,
    'salad': 70,
    'water': 30,
}

print("WELCOME TO OUR RESTAURANT")
print("Here's our menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

order_total = 0
order_items = []

while True:
    item = input("Enter the name of item you want to order: ").strip()
    if item in menu:
        order_total += menu[item]
        order_items.append(item)
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry, '{item}' is not available.")

    another = input("Do you want to order another item? (yes/no): ").strip().lower()
    if another != "yes":
        break

print("\nYour order summary:")
for item in order_items:
    print(f"- {item}: Rs {menu[item]}")
print(f"Total amount to pay: Rs {order_total}")





#conconcession stand program

menu = {
    "momo": 200,
    "lapghing": 60,
    "chatpate": 50,
    "keema noodles": 160,
    "alu chips": 50,
    "panipuri": 50,
    "soda": 20
}
cart = []
total = 0

print("--------------MENU----------------")
for key, value in menu.items():
    print(f"{key:15}: Rs{value:.2f}")
print("----------------------------------")

while True:
    food = input("Select an item from the menu (q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("--------------Your order is------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=",")
print()
print(f"Your total is: {total:.2f}")

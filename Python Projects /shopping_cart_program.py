#shoping cart program
foods = []
prices = []
total = 0

while True:
    food_item = input("Enter a food you want to buy (q to Quit): ")
    if food_item.lower() == "q":
        break
    else:
        price_food = float(input(f"Enter the price of the {food_item}: Rs "))
        foods.append(food_item)
        prices.append(price_food)

print("---------Your Cart ----------")

for food_item in foods:
    print(food_item, end= " ")

for price_food in prices:
    total += price_food

print() #TO PRINT THE BELOW LINE IN NEW LINE
print (f"Your total is Rs {total}")





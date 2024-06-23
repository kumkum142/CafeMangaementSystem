print("\n")
print("========================== Welcome To MY Restaurant ==============================")
print("\n")

menu = [
         "\t \t \t Dishes \t \tPrices \n",
         "\t \t \t ‾‾‾‾‾‾ \t \t‾‾‾‾‾‾ \n",
         "\t \t \t Pizza \t \t         ₹ 80 \n",
         "\t \t \t Coffee \t \t ₹ 40 \n",
         "\t \t \t Tea \t \t         ₹ 20 \n",
         "\t \t \t Fried Poha \t \t ₹ 60 \n",
         "\t \t \t Noodles \t \t ₹ 90 \n",
         "\t \t \t Fries \t \t         ₹ 50 \n",
         "\t \t \t Ice Cream \t \t ₹ 30 \n",
         "\t \t \t Pasta \t \t         ₹ 30 \n",
         "\t \t \t Sandwich \t \t ₹ 40 \n",
         "\t \t \t Chocolate Shake \t ₹ 60 \n\n"
]

for item in menu:
    print(item)

prize = {
    "Pizza": 80,
    "Coffee": 40,
    "Tea": 20,
    "Fried Poha": 60,
    "Noodles": 90,
    "Fries": 50,
    "Ice Cream": 30,
    "Pasta": 30,
    "Sandwich": 40,
    "Chocolate Shake": 60
}

total_price = 0
ordered_dishes = []

dish_number = int(input("Enter number of dishes: "))
print("\n")

for _ in range(dish_number):
    order = input("Enter your dish: ")
    if order in prize:
        ordered_dishes.append(order)
        print(f"Your ordered dish {order} has been booked\n")
        total_price += prize[order]
    else:
        print(f"Sorry!! {order} is not available.\n")

print("\n")
another_order = input("Do you want to add another dish? (Yes/No): ")
print("\n")

if another_order.lower() == "yes":
    another_order = input("Enter more dish: ")
    if another_order in prize:
        ordered_dishes.append(another_order)
        total_price += prize[another_order]
    else:
        print(f"Sorry!! {another_order} is not available.\n")

print("\n")
print("========== Bill ==========\n")

print("Dishes \t \t \t Prizes")
print("‾‾‾‾‾‾ \t \t \t ‾‾‾‾‾‾")

for dish in ordered_dishes:
    print(f"{dish} \t \t ₹ {prize[dish]}")

print("----------------------------------")

print(f"Total Amount \t \t  ₹ {total_price}")
print("\n")

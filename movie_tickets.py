
# Getting input
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

# Determining price by age.
if age<13:
    price = 300
    print(f"Price = {price}")
elif age >= 13 and age <= 17:
    price = 400
    print(f"Price = {price}")
else:
    price = 600
    print(f"Price = {price}")

# Adding the discount if the day of the week is on Tuesday.
if day.lower() == "tuesday":
    discount_price = (price - 100)
    print(f"Discounted price for Tuesday = {discount_price}")

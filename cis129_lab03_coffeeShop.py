# Coffee Shop Receipt Program
# Created by Michaela Brady
# This program calculates the total cost of coffee and muffins, including tax.


# Get the user input
coffee = int(input("How many coffees would you like to purchase? "))
muffins = int(input("How many muffins would you like to purchase? "))
croissants = int(input("How many croissants would you like to purchase? "))
tea = int(input("How many teas would you like to purchase? "))

# Calculate the subtotal, tax, and total
subtotal = (coffee * 5) + (muffins * 4) + (croissants * 3) + (tea * 2.50)
tax = subtotal * 0.06
total = subtotal + tax

# Print the receipt
print("***************************************")
print("Sunshine Coffee Shop Receipt")

# Print each coffee as a separate line
for i in range(coffee):
    print(f"1 Coffee for $5.00")

# Print each muffin as a separate line
for i in range(muffins):
    print(f"1 Muffin for $4.00")

# Print each croissant as a separate line
for i in range(croissants):
    print(f"1 Croissant for $3.00")

# Print each tea as a separate line
for i in range(tea):
    print(f"1 Tea for $2.50")

# Print the tax and total
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")

# Thank you message
print("Thank you for your purchase. Have a nice day!")

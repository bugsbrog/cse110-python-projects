# Added a tip % (as a decimal) and added the tip % to the total and made it so people can choose the currency symbol they want

# Ask for price of child's meal (floating point)
child_meal = float(input("What is the price of a child's meal? "))

# Ask for price of adult's meal (floating point)
adult_meal = float(input("What is the price of an adult's meal? "))

# Ask for number of children (integer)
children = int(input("How many children are there? "))

# Ask for number of adults (integer)
adults = int(input("How many adults are there? "))

currency_symbol = input("What currency symbol would you like to use? ($, €, £, etc.) ")

# Determine meal's subtotal by * number of children by price of meal & * number of adults by price of meal & + children subtotal & adult subtotal together
meal_subtotal = (children * child_meal) + (adults * adult_meal)

# Print the subtotal
print(f"Subtotal: {currency_symbol}{meal_subtotal:.2f}")

# Ask for sales tax rate as % (floating point)
sales_tax_rate = float(input("What is the sales tax rate? "))

# Subtotal * sales tax rate / 100
sales_tax = meal_subtotal * sales_tax_rate / 100

# Print sales tax
print(f"Sales Tax: {currency_symbol}{sales_tax:.2f}")

# Tip Percentage
tip = float(input("How much would you like to tip? (enter as a decimal) "))

# Calculate tip amount
tip_amount = meal_subtotal * tip

# Add subtotal, sales tax, & tip amount
total = meal_subtotal + sales_tax + tip_amount

# Print total
print(f"Total: {currency_symbol}{total:.2f}")

# Ask user for payment amount (floating point)
payment_amount = float(input("What is the payment amount? "))

# Calculate the change
change_back = payment_amount - total

# Print the change
print(f"Change: {currency_symbol}{change_back:.2f}")
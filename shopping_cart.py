# Added spacing to the shopping cart display so the prices line up

print("Welcome to the Shopping Cart Program!")

# empty list
cart_items = []
cart_prices = []

while True:
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = input("Please enter an action: ")

# 1. Add a new item (.append)
    if choice == "1":
        add_item = input("What item would you like to add? ")
        cart_items.append(add_item)
        add_price = float(input(f"What is the price of '{add_item}'? "))
        cart_prices.append(add_price)
        print(f"'{add_item}' has been added to the cart.")

# 2. Display contents of shopping cart
    elif choice == "2":
        print("The contents of the shopping cart are: ")
        for i in range(len(cart_items)):
           cart = cart_items[i]
           price = cart_prices[i]
           print(f"{i + 1}. {cart:15} ${price:.2f}")

# 3. Remove an item (only needed for the final project deliverable)
    elif choice == "3":
        print("The contents of the shopping cart are: ")
        for i in range(len(cart_items)):
            cart = cart_items[i]
            price = cart_prices[i]
            print(f"{i + 1}. {cart} - ${price:.2f}")
        print()
        remove_item = int(input("Which item would you like to remove? "))

        if remove_item >= 1 and remove_item <= len(cart_items):
            real_index = remove_item - 1
            cart_items.pop(real_index)
            cart_prices.pop(real_index)
            print("Item removed.")
        else:
            print("Sorry, that is not a valid item number.")

# 4. Compute the total (only needed for the final project deliverable)
    elif choice == "4":

        # counter
        running_total = 0

        for price in cart_prices:
            running_total += price

        print(f"The total price of the items in the shopping cart is ${running_total:.2f}")

# 5. Quit
    elif choice == "5":
        print("Thank you. Goodbye.")
        break
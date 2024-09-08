# Title: Grocery Shopping List Creator

# Initialize variables
place = None  # Variable to store the grocery store location
total = 0     # Variable to keep track of the total cost of items
price = 0     # Variable to store the price of each item

while place != 'quit':
    # Prompt the user for the grocery store location or 'quit' to exit
    place = input('Where are you grocery shopping (type "quit" to exit): ')

    # Exit the loop if the user types 'quit'
    if place == 'quit':
        break

    grocery_list = []  # List to store items and their prices for the current grocery store

    while True:
        # Prompt the user to enter an item or press Enter to finish
        item = input('Enter what you have purchased (or press Enter to finish): ')

        # Exit the inner loop if the user does not enter an item
        if not item:
            break

        # Prompt the user to enter the price of the item
        price = float(input('Enter the price of the item: '))
        grocery_list.append((item, price))  # Store item and price as a tuple in the list
        total += price  # Add the price to the total cost

    # Write the grocery list to a file named after the grocery store location
    with open(f"{place}.txt", "w") as f:
        # Write each item and its price to the file
        for item, price in grocery_list:
            f.write(f"{item}: ${price:.2f}\n")
        # Write the total cost at the end of the file
        f.write(f"\nTotal: ${total:.2f}\n")

    # Inform the user that the grocery list has been saved
    print(f"Grocery list saved to {place}.txt")
    total = 0  # Reset the total cost for the next grocery store

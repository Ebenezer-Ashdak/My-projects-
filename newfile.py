# Define a dictionary of items and their prices
prices = {
    "apple": 1.50,
    "banana": 0.50,
    "milk": 2.00,
    "bread": 1.20
}

# Initialize variables
total_cost = 0
items_sold = []

# Function to display receipt
def display_receipt(items, cost, discount_amount):
    print("\n--- Sales Receipt ---")
    for item, qty, price in items:
        print(f"{qty}x {item}: ${price * qty:.2f}")
    print("-" * 20)
    print(f"Subtotal: ${cost:.2f}")
    if discount_amount > 0:
        print(f"Discount: -${discount_amount:.2f}")
        print(f"Total:    ${cost - discount_amount:.2f}")
    else:
        print(f"Total:    ${cost:.2f}")
    print("---------------------")

# Main sales loop
while True:
    item_name = input("Enter item name (or 'done' to finish): ").lower()
    if item_name == 'done':
        break
    if item_name in prices:
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
            item_price = prices[item_name]
            items_sold.append((item_name, quantity, item_price))
            total_cost += item_price * quantity
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
    else:
        print(f"Item '{item_name}' not found.")

# Apply discount (example: 10% discount if total cost > $20)
discount_rate = 0.10
min_cost_for_discount = 20
discount = 0
if total_cost > min_cost_for_discount:
    discount = total_cost * discount_rate
    print(f"\nDiscount of {discount_rate*100}% applied!")

# Display the final receipt
display_receipt(items_sold, total_cost, discount)
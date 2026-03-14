print("----------- Products Purchase ---------------")

items = []
total_price = 0

# Loop for 3 items
for i in range(1, 4):
    print(f"\nItem {i}")
    item_name = input("Enter item name: ")
    price = float(input(f"Enter price of {item_name}: "))
    quantity = int(input("Enter quantity purchased: "))
    
    total = price * quantity
    total_price += total
    
    print(f"The total cost of {item_name} purchased is {total:.2f} cedis")
    items.append(item_name)

print("\n-----------------------------------")
print(f"Total amount before discount: {total_price:.2f} cedis")

# Discount section
discount_rate = 0.50  # 50%
membership = input("Do you have a membership? (yes/no): ").lower()

if membership == "yes":
    discount_amount = total_price * discount_rate
    final_price = total_price - discount_amount
    
    print("\nCongratulations! You received a 50% discount.")
    print(f"Discount amount: {discount_amount:.2f} cedis")
    print(f"Total amount to pay: {final_price:.2f} cedis")

else:
    print("\nYou are not eligible for a discount.")
    print(f"Total amount to pay: {total_price:.2f} cedis")
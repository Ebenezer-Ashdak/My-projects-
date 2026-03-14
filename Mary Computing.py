# Electricity Bill Calculator (ECG Style)
# Author: Student
# Purpose: Calculate monthly electricity bill

def calculate_bill(units):
    fixed_charge = 20.00
    bill = 0

    if units <= 50:
        bill = units * 0.50
    elif units <= 150:
        bill = (50 * 0.50) + ((units - 50) * 0.75)
    else:
        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)

    total_bill = bill + fixed_charge
    return total_bill


while True:
    print("\n===== ELECTRICITY BILL MENU =====")
    print("1. Calculate Electricity Bill")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        meter_number = input("Enter Meter Number: ")

        if meter_number == "":
            print("Invalid meter number!")
            continue

        try:
            units = float(input("Enter Units Consumed: "))
            if units < 0:
                print("Units cannot be negative!")
                continue
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        total = calculate_bill(units)

        print("\n----- MONTHLY BILL STATEMENT -----")
        print(f"Meter Number     : {meter_number}")
        print(f"Units Consumed   : {units}")
        print("Fixed Charge     : GHS 20.00")
        print(f"Total Bill       : GHS {total:.2f}")
        print("--------------------------------")

    elif choice == "2":
        print("Thank you for using the Electricity Bill Calculator.")
        break
    else:
        print("Invalid choice! Please select 1 or 2.")
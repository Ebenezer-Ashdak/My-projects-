print(".       ------------------------------ Project 17 ----------------------------")
print(".   ------------------------------ Nelvin Currency Converter Project ----------------------------")
print(". ------------------------------ Currency 💲 Converter System ----------------------------")

value_of_cedis = "¢"
value_of_dollar = "$"
value_of_euro = "€"
value_of_rupees = "₹"

money = float(input("Enter amount to be converted:    "))
currency = input("Enter your currency (cedis, dollar, rupees, euro) 💲:    ").lower()
target_currency = input("Select your target currency 💵 (cedis, dollar, rupees, euro):    ").lower()

print("-------------------------------------------------------------")

# If same currency
if currency == target_currency:
    print("No conversion needed.")
    print("You still have: " + str(money))

# Conversion from cedis
elif currency == "cedis" and target_currency == "dollar":
    conversion = money * 0.074
    print("Your money has been converted from cedis to dollars.")
    print("You now have: " + value_of_dollar + str(round(conversion,2)))

elif currency == "cedis" and target_currency == "euro":
    conversion = money * 0.068
    print("Your money has been converted from cedis to euro.")
    print("You now have: " + value_of_euro + str(round(conversion,2)))

elif currency == "cedis" and target_currency == "rupees":
    conversion = money * 6.15
    print("Your money has been converted from cedis to rupees.")
    print("You now have: " + value_of_rupees + str(round(conversion,2)))

# Conversion from dollar
elif currency == "dollar" and target_currency == "cedis":
    conversion = money / 0.074
    print("Your money has been converted from dollars to cedis.")
    print("You now have: " + value_of_cedis + str(round(conversion,2)))

elif currency == "dollar" and target_currency == "euro":
    conversion = money * 0.92
    print("Your money has been converted from dollars to euro.")
    print("You now have: " + value_of_euro + str(round(conversion,2)))

elif currency == "dollar" and target_currency == "rupees":
    conversion = money * 83
    print("Your money has been converted from dollars to rupees.")
    print("You now have: " + value_of_rupees + str(round(conversion,2)))

# Conversion from euro
elif currency == "euro" and target_currency == "cedis":
    conversion = money / 0.068
    print("Your money has been converted from euro to cedis.")
    print("You now have: " + value_of_cedis + str(round(conversion,2)))

elif currency == "euro" and target_currency == "dollar":
    conversion = money * 1.08
    print("Your money has been converted from euro to dollar.")
    print("You now have: " + value_of_dollar + str(round(conversion,2)))

elif currency == "euro" and target_currency == "rupees":
    conversion = money * 90
    print("Your money has been converted from euro to rupees.")
    print("You now have: " + value_of_rupees + str(round(conversion,2)))

# Conversion from rupees
elif currency == "rupees" and target_currency == "cedis":
    conversion = money / 6.15
    print("Your money has been converted from rupees to cedis.")
    print("You now have: " + value_of_cedis + str(round(conversion,2)))

elif currency == "rupees" and target_currency == "dollar":
    conversion = money / 83
    print("Your money has been converted from rupees to dollars.")
    print("You now have: " + value_of_dollar + str(round(conversion,2)))

elif currency == "rupees" and target_currency == "euro":
    conversion = money / 90
    print("Your money has been converted from rupees to euro.")
    print("You now have: " + value_of_euro + str(round(conversion,2)))

else:=
    print("Invalid currency entered ")
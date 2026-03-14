
while True:
    house_name=(input("Enter house name:"))
    meter_number=int(input("Enter Meter number:"))
    units_of_electricity_used=float(input("Enter units of electricity used:"))

    if units_of_electricity_used<=50:
        bills=units_of_electricity_used*1.0
    
    else:
        bills=units_of_electricity_used*1.5 
    
    print("-------------------------------------------------------------------------------------------------------------")
    print("/n bills summary")
    print("house_name:",house_name)
    print("meter_number:",meter_number)
    print("units_of_electricity_used:",units_of_electricity_used)
    print("bills:",bills)
    print("-------------------------------------------------------------------------------------------------------------")          

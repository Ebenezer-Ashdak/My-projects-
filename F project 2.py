print ("                       ------------------------- PROJECT NINE(9) --------------------------")
print("             ------------------------- Farm Produce Sales Calculator ------------------------------")
print("           ------------------------------  SALE RECORDS ⏺️ ---------------------------------------")
print("           ------------------------------  FIRDUSE PROJECT (9) ---------------------------------------")


#A farmer struggle with profit calculation, so a python program is to be generated to solve this problem

# 1.Data on crop products are collected
# Market price of farm produce is requested 
#.Number of bags of farm produce sold is requested and total price is generated
# The total amount gotten from the sales is calculated and printed out 

# 2. With the data collected the revenue is asked weather to be generated
#If answer is yes the revenue is provided but if no an expression of displeasure is displayed 
#And if anything other than yes or no is inputed the program displays an error 
# Adding of the total amount of sold product 
# Revenue for previous months is requested 
#Determinig of profit or loss based on revenue between the previous and current month that is
#If the revenue for the previous month is greater than the revenue of the current month, the farmer has made a loss
#And if the revenue of the current month is greater than that of the previous month, a profit is made

#Data on crop produce are collected and a standard price is generated 
Maize= float(input("Market price of maize:    "))
number_sold = float(input("Enter number of sold:    "))
Maize_total = Maize  * number_sold
print("Total amount sold in month:     " + str(Maize_total) + " cedis")


Beans = float(input("Market price of beans:    "))
number_sold = float(input("Enter number of sold:    "))
Beans_total = Beans* number_sold
print("Total amount sold in month:     " + str(Beans_total) + " cedis")


Rice = float(input("Market price of rice:    "))
number_sold = float(input("Enter number of sold:    "))
Rice_total = Rice * number_sold
print("Total amount sold in month:     " + str(Rice_total) + " cedis")


#A conditional Statement weather revenue should be generated 
revenue_1 = Rice_total + Beans_total + Maize_total
revenue = input("Would you like to view the revenue of the month(yes , no):    ")
if revenue == "yes":
    print("The revenue for the month is:    " + str(revenue_1))
elif revenue == "no":
    print("😤😠")
else:
    print ("Invalid input ! ⚠️")   
    
#Generation of profit and loss
previous_month_revenue =float(input("Enter revenue for previous month:    "))
if revenue_1 > previous_month_revenue:
    profit = revenue_1 - previous_month_revenue
    print("You gained a profit of:    " + "GHC" + str(profit))
elif revenue_1 < previous_month_revenue:
    loss = previous_month_revenue - revenue_1
    print ("You've made a loss of:    " + "GHC" + str(loss))
print ("done")
#$codesource ebexion_ashdak$ 
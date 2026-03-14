options =  ["borrow", "return"]

user_input = input("Type borrow /return or Q to quit: ")
if user_input == "q":
    print("")
if user_input == "borrow":
        name_book1 = input("Name of book:    ")
        borrower1 = input("Name of borrower:    ")
        date1 = input("Today's date:    ")
        date_return1 = input("Date to return the book:    ")
        print (borrower1+" borrowed the book "+name_book1+" and is to return the book on the "+date_return1)
elif user_input == "return":
     name_book = input("Name of book:    ")
     returner = input("Name of returner:    ")
     date_return = input("Date the book has been returned:    ")
     date_taken = input("Date the book was taken:    ")
     length_return1 = int(input("How long before the book was returned :    "))
     #length_return = int(length_return1)  
     if length_return1 >= 20:
         print("")
         print("Prepare for punishment")
     elif  length_return1 < 20:
        print("You have returned the book on time !")
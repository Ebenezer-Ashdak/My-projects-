import random

user_wins = 0
computer_wins = 0

options =  ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ")
    if user_input == "q":
        break
        
    if user_input not in options:
        continue #runs line 9 until a desired input is gotten
        
    random_number = random.randint(0, 2)
    
    computer_pick = options[random_number]
    print("Computer picked", computer_pick , ".")
    
    
    if user_input == "rock" and computer_pick == "scissors":
       print("You win!")
       user_wins == 1
       continue
       
    elif user_input == "scissors" and computer_pick == "paper":
       print("You win!")
       user_wins == 1
       continue   
       
    elif user_input == "paper" and computer_pick == "rock":
       print("You win!")
       user_wins == 1
       continue 
       
    elif user_input == "paper" and computer_pick == "paper":
       print("draw!")
       user_wins == 0
       continue
       
    elif user_input == "rock" and computer_pick == "rock":
       print("draw!")
       user_wins == 0
       continue
    
    elif user_input == "scissors" and computer_pick == "scissors":
       print("draw!")
       user_wins == 0
       continue                                           
    else:
       print("You lost")
       computer_wins == 1
       
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Thanks for playing")
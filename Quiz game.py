print("Welcome to my Python Quiz Game!")
print("You will be asked a series of questions. Answer them as best as you can.")

playing = input("Would you like to play? (yes/no): ")

if playing.strip().lower() != "yes":
    print("No worries! Maybe next time. Goodbye!")
    quit()

print("Great! Let's get started. 😊\n") 
  
answer = input("Question 1: What does 'CPU' stand for?\nYour answer: ")
print(f"You answered: '{answer}'")

if answer.strip().lower() == "central processing unit":
    print('Correct! Well done!')
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")  

print("\nYou've completed the quiz. Thank you for playing!")      

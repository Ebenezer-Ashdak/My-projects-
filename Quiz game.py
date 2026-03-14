print("Welcome to my python quiz game")

playing = input("Do you want to play?  ")

if  playing.lower()  != "yes":
    quit()
print("Alright let's play :)") 
  
answer = input("What does CPU stand for? ")
if  answer == "central processing unit":
    print('correct')
else:
    print('Incorrect')  
print("Done")      
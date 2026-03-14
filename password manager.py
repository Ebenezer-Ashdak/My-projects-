from getpass import getpass 

pwd = input("what is the master password?    ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data= line.rstrip()
            user, passw = data.split("|")
            
def add():
    name = input("Account Name:    ")
    pwd = input (getpass("Password:    "))
    
    with open("passwords.txt", 'a') as f: 
        f.write(name + "|" + pwd + "\n" )
while True:
    mode = input("Would you like to add a new password or view existing ones(view,add) or press q to quit:    ")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode')
        continue
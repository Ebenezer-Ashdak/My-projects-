import random
import string

def generate_password(length):
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for password length
try:
    length = int(input("Enter desired password length: "))
    if length < 6:
        print("Password length should be at least 6 for security.")
    else:
        print("Generated password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
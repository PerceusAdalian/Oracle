import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

while True:
    response = str(input("Would you like to generate a new password? [y/n/exit] "))
    if response == "y":
        try:
            length = int(input("Input the desired length of the password: "))
            if length <= 0:
                print("Desired length is 0, therefore, there is no possible password to generate; please try again.")
                continue
            else:
                password = generate_password(length)
                print("Generated Password: ", password)
        except ValueError: 
            print("Invalid Input, please try again.")
            continue
    elif response == "n":
        break
    elif response == "exit":
        break
    else:
        break
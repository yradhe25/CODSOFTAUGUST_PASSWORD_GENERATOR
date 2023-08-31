import string
import random

def generate_password():
    alphabets=string.ascii_letters
    digits=string.digits
    punctuations=string.punctuation
    letters=alphabets+digits+punctuations

    while True:
        length=0
        try:
            length=int(input("Enter the length of the password : "))
            if length<0:
                print("Password length cannot be less than 0")
                continue
        except ValueError:
            print("Please enter a valid length!")
            continue

        characters=[]

        for i in range(length):
            rl=random.choice(letters)
            characters.append(rl)

        password=''.join(characters)
        print(f"Your password is {password}")

        again=input("Do you want to generate another password ? ( Y/N ) : ")

        while again.upper() not in("Y","N"):
            print("Please enter a valid choice!")
            again=input("Do you want to generate another password ? ( Y/N ) : ")

        if again.upper()=="Y":
            continue

        elif again.upper()=="N":
            print("Thank you for using the Password Generator. Goodbye!")
            break

generate_password()
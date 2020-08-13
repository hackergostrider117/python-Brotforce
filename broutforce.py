import random

passwrod = str(input("enter password onley numbers 4 diggits : "))

guess = " "

while guess != passwrod:
    guess = str(random.randint(0,9999))

    print("=> "+ guess)

    if(guess == passwrod):
        print("the passwrod1 is :"+ passwrod)
        break
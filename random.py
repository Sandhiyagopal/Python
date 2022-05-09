import random
import randint
seed(1)
guess=int(input("enter the guess number:"))
for i in range(2):
    value=randint(1,10)
    if guess==value:
        print("well guessed")
    else:
        print("try again")
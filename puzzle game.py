import random

while True:
    choice= ["rock","paper","scissors"]
    computer=random.choice(choice)
    user=None
    while user not in choice:
        user=input("rock, paper or scissors: ?").lower()

    print("computer pick:",computer)
    print("you pick :",user)
    print("*-----------------")
    if user==computer:
        print("the game is tie!")
    elif user=="rock":
        if computer=="paper":
            print("you lose!")
        elif computer=="scissors":
            print("you win!")
    elif user=="paper":
        if computer=="scissors":
            print("you lose!")
        elif computer=="rock":
            print("you win!")
    elif user== "scissors":
        if computer== "rock":
            print("you lose!")
        elif computer== "paper":
            print("you win!")
    decision=input("do you want to play again (yes or no):?").lower()
    if decision!="yes":
        break
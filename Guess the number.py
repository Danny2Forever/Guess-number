import random

def guess():
    players = int(input("How many players : "))
    number = random.randint(1,100)
    status = 0
    while(status == 0):
        for i in range(1,players+1):
            if(status == 0):
                guess = int(input("Player "+str(i)+" guess your number : "))
                if(guess > number):
                    print("Your number Too Big")
                if(guess < number):
                    print("Your number Too Small")
                if(guess == number):
                    print("You are the winner")
                    status = 1
    return status

if guess() == 1:
    reset = input("Do you wanna play again? Y/n : ")
    if reset == "Y" :
        guess()
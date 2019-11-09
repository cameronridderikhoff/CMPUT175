#Cameron Ridderikhoff  
#March 16, 2017
#Lab 8: Player guesses a number between 1-100
import random
def main():
    number=random.randint(1, 100)
    numGuesses=6
    right=False
    while numGuesses>0 and not right:
        guess=int(input("Guess a Number Between 1-100: "))
        if guess==number:
            right=True
        elif guess>number:
            print("Too high!")
        else: #guess<number
            print("Too Low!")
        numGuesses-=1
    if right:
        print("Hooray, you win!")
    else:
        print("Oh no! You lost, the correct number is "+str(number))
    
main()
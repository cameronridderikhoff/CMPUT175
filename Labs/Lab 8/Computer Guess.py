#Cameron Ridderikhoff  
#March 16, 2017
#Lab 8: Computer guesses a number between 1-100
import random
def main():
    numList=[]
    for i in range(1,100):
        numList.append(i)
    print("Think of a number between 1-100.")
    highest=99
    lowest=1
    mid=(highest+1)//2
    correct=False
    print('Type "+" if the number is too low, "-" if too high, "win" if I have guessed the number, and "quit" to quit')
    userIn=""
    
    while not correct and userIn.lower()!="quit":
        print(str(highest))
        print(str(lowest))
        print(str(mid))
        print("Is it "+str(mid)+"?") 
        userIn=input()
        if userIn.lower()=="win":
            correct=True        
        elif userIn=="+":#we need a larger number
            lowest=mid+1
            mid=(highest+mid+1)//2
        elif userIn=="-":#we need a smaller num
            highest=mid-1
            mid=(lowest+mid+1)//2
        elif userIn.lower()=="quit":
            pass
        else:
            print("Invalid Input")
            
    if correct:
        print("Hooray, computers will rule the world!")
    else:
        print("You chose to quit before I had the chance to guess!")
    
main()
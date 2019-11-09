# CMPUT 175 Winter 2013 Lab 3 Exercise 1
# This program is used "browse the web"
#Cameron Ridderikhoff

# A Stack implementation

class Stack:
    def __init__(self):
        self.__items = []
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        return self.__items.pop()
    def peek(self):
        return self.__items[len(self.__items)-1]
    def isEmpty(self):
        return len(self.__items) == 0
    def size(self):
        return len(self.__items)
    
    
def browse():
    backStack=Stack()
    forStack=Stack()
    user="www.cs.ualberta.ca"
    print("Starting at homepage: "+user)
    currentPage=user
    while user != "QUIT":
        user=input()
        if user == "<":
            if not backStack.isEmpty():
                forStack.push(currentPage)
                currentPage=backStack.pop()
                print("Current Page: "+currentPage)
            else:
                print(user+" is an invalid action")
        elif user == ">":
            if not forStack.isEmpty():
                backStack.push(currentPage)
                currentPage=forStack.pop()
                print("Current Page: "+currentPage)
            else:
                print(user+" is an invalid action")
        else:
            while not forStack.isEmpty():
                forStack.pop()
            print("Current Page: "+user)
            backStack.push(currentPage)
            currentPage=user
browse()
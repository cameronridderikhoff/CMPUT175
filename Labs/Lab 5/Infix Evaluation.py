#CMPUT 175
#Lab 5: Infix to Postfix and Evaluate
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
    
def inToPost(string):
    #This function turns an infix expression into a postfix expression
    #Only works for operands that are numbers
    operators=Stack()
    string=''.join(string.split())
    postfix=[]
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["%"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    for token in string:
        if token in "0123456789":
            postfix.append(token)
        elif token=="(":
            operators.push(token)
        elif token==")":
            operator=operators.pop()
            while not operators.isEmpty() and operator!="(":
                postfix.append(operator)
                operator=operators.pop()
        else:
            while not operators.isEmpty() and prec[token]<=prec[operators.peek()]:
                postfix.append(operators.pop())
            operators.push(token)
            
    while not operators.isEmpty():
        postfix.append(operators.pop())
    return postfix

def postEvaluation(expression):
    #This function evaluates a postfix expression given by the
    #"inToPost()" method
    operands=Stack()
    
    for token in expression:
        if token in "0123456789":
            operands.push(token)
        else:
            if token=="+":
                second=int(operands.pop())
                first=int(operands.pop())
                operands.push(first+second)
            elif token=="-":
                second=int(operands.pop())
                first=int(operands.pop())
                operands.push(first-second)
            elif token=="*":
                second=int(operands.pop())
                first=int(operands.pop())
                operands.push(first*second)
            elif token=="/":
                second=int(operands.pop())
                first=int(operands.pop())
                try:
                    operands.push(first/second)
                except ZeroDivisionError:
                    print("There is a division by zero in this expression. Please fix the expression")
            elif token=="%":
                second=int(operands.pop())
                first=int(operands.pop())
                try:
                    operands.push(first%second)
                except ZeroDivisionError:
                    print("There is a division by zero in this expression. Please fix the expression") 
                    
    return operands.pop()

def main():
    f=open("afile.txt", "r")
    ls=f.read()
    expressions=ls.splitlines()
    for expression in expressions:
        postfix=inToPost(expression)
        print(postfix)
        print(postEvaluation(postfix))
    
main()
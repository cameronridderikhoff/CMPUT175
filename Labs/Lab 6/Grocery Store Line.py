#The Queue Class
class Queue:
    def __init__(self):
        self.items=[]
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items)<1:
            raise IndexError("The Queue is empty, you can't dequeue!")
        else:
            return self.items.pop(0)
        
    def peek(self):
        if len(self.items)<1:
            raise IndexError("The Queue is empty, you can't peek!")
        else:
            return self.items[0]  
    
    def isEmpty(self):
        return len(self.items)==0  
    
    def clear(self):
        self.items=None
        self.items=[]
    
    def __str__(self):
        return "A queue with items " + str(self.items)

def main():
    normQ=Queue()
    vipQ=Queue()
    uinput=input("'add' - add new customer, 'serve' - serve the next customer, or 'quit' - quit the program\n")
    while uinput.lower()!="quit":
        if uinput.lower()=="add":
            name=input("What is this person's name?: ")
            if not len(vipQ.items)>2:
                isVIP=input("Are they a VIP (y/n)?: ")
                if isVIP.lower()=="y":
                    vipQ.enqueue(name)
                    print("People in the VIP queue: "+str(vipQ))
                    print("People in the normal queue: "+str(normQ))
                else:
                    if not len(normQ.items)>2:
                        normQ.enqueue(name)
                        print("People in the VIP queue: "+str(vipQ))
                        print("People in the normal queue: "+str(normQ))                        
                    else:
                        print("Error, the normal Queue is full")
            elif not len(normQ.items)>2:
                print("The VIP queue was full, so we put them in the normal queue")
                normQ.enqueue(name)
                print("People in the VIP queue: "+str(vipQ))
                print("People in the normal queue: "+str(normQ))                
            else:
                print("Error, both Queues are full")
        elif uinput.lower()=="serve":
            if not vipQ.isEmpty():
                vipQ.dequeue()
                print("People in the VIP queue: "+str(vipQ))
                print("People in the normal queue: "+str(normQ))                
            else:
                try:
                    normQ.dequeue()
                    print("People in the VIP queue: "+str(vipQ))
                    print("People in the normal queue: "+str(normQ))                    
                except:
                    print("Both queues are empty!")   
        else:
            print("You didn't enter proper input.")
        uinput=input("'add' - add new customer, 'serve' - serve the next customer, or 'quit' - quit the program\n")

main()
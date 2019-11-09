#Lab 6
#Cameron Ridderikhoff
#March 2, 2017

import datetime, time
#The Bounded Queue Class
class BQueue:
    def __init__(self, capacity):
        self.items=[]
        self.size=capacity
        
    def enqueue(self, item):
        if len(self.items)+1>self.size:
            raise IndexError("The Queue is full, you can't add anymore!")
        else:
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
    
    def isFull(self):
        return len(self.items)==self.size   
    
    def getCapacity(self):
        return self.size
    
    def clear(self):
        self.items=None
        self.items=[]
    
    def __str__(self):
        return "A queue with items " + str(self.items)
    
#The Circular Queue Class
class CQueue:
    def __init__(self, capacity):      
        self.items=[]
        self.capacity=capacity
        self.size=0 #size is how many items are currently in the queue
        self.head=0
        self.tail=0
        
    def enqueue(self, item):
        if self.size+1>self.capacity:
            raise IndexError("The Queue is full, you can't add anymore!")
        else:
            if len(self.items)+1>self.capacity:
                self.items.insert(tail, item)
            else:
                self.items.append(item)
            self.size+=1
            self.tail=(self.tail+1)%self.capacity
    
    def dequeue(self):
        if self.size<1:
            raise IndexError("The Queue is empty, you can't dequeue!")
        else:
            temp=self.items[self.head]
            self.items[self.head]=None
            self.size-=1
            self.head= (self.head+1)%self.capacity
            return temp
        
    def peek(self):
        if self.size<1:
            raise IndexError("The Queue is empty, you can't peek!")
        else:
            return self.items[self.head]  
    
    def isEmpty(self):
        return self.head==self.tail
    
    def isFull(self):
        return self.size==self.capacity
    
    def getCapacity(self):
        return self.capacity
    
    def getSize(self):
        return self.size
    
    def clear(self):
        self.items=None
        self.items=[]
        self.size=0
        self.head=0
        self.tail=0
    
    def __str__(self):
        return "A queue with items " + str(self.items)    
    
def main():
    capacity=20000
    cQ=CQueue(capacity)
    bQ=BQueue(capacity)
    for i in range(capacity):
        cQ.enqueue(i)
        bQ.enqueue(i)
    
    cQTimeBeg=float(str(datetime.datetime.time(datetime.datetime.now())).split(":")[2])
    for i in range(capacity):
        cQ.dequeue()
    cQTimeEnd=float(str(datetime.datetime.time(datetime.datetime.now())).split(":")[2])
    cQTime=cQTimeEnd-cQTimeBeg
    print("Circular Queue: "+str(cQTime))
    
    bQTimeBeg=float(str(datetime.datetime.time(datetime.datetime.now())).split(":")[2])
    for i in range(capacity):
        bQ.dequeue()
    bQTimeEnd=float(str(datetime.datetime.time(datetime.datetime.now())).split(":")[2])
    bQTime=bQTimeEnd-bQTimeBeg
    print("Bounded Queue: "+str(bQTime)) 
    print("Bounded Queue minus Circular Queue: "+str(bQTime-cQTime))
main()
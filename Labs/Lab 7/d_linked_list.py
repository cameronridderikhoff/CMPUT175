from d_linked_node import d_linked_node

class d_linked_list:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0        

            
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        #add the node at  the front of the list
        if self.head != None:
            temp=self.head
            node=d_linked_node(item, temp, None)
            temp.setPrevious(node)
            self.head=node
            self.size+=1
        else:
            node=d_linked_node(item, None, None)
            self.head=node
            self.tail=node
            self.size+=1
    
    def remove(self, item):
        current=self.head
        #check the first item in the list
        if current.getData()==item:
            if current.getNext()==None:
                self.head=None
                self.size-=1
            else:
                self.head=current.getNext()
                self.size-=1
       #check the rest of the list, excluding the last node 
        found=False
        while current.getNext() != None and not found:
            current=current.getNext()
            if current.getData() == item:
                if current.getNext()==None:
                    current.getPrevious().setNext(current.getNext())
                    self.tail=current.getPrevious()
                    found=True
                    self.size-=1
                else:
                    current.getPrevious().setNext(current.getNext())
                    current.getNext().setPrevious(current.getPrevious())
                    found=True
                    self.size-=1
        
    def append(self, item):
        if self.head!=None:
            temp=self.tail
            node=d_linked_node(item, None, temp)
            temp.setNext(node)
            self.tail=node
            self.size+=1
        else:
            node=d_linked_node(item, None, None)
            self.head=node
            self.tail=node
            self.size+=1
        
    def insert(self, pos, item):
        current=self.head
        i=0
        if pos==i and current==None:#position 0, nothing at the head
            node=d_linked_node(item, None, None) 
            self.head=node  
            self.size+=1        
        while current.getNext()!=None and i<pos:
            current=current.getNext()
            i+=1
        if i==pos:
            if pos==0:#position 0
                node=d_linked_node(item, current, None) 
                self.head=node
                current.setPrevious(node)
                self.size+=1
            elif current.getNext()==None:#end of the list, insert here
                prev=current.getPrevious()
                node=d_linked_node(item, current, current.getPrevious()) 
                prev.setNext(node)
                current.setPrevious(node)
                self.size+=1
            else:#anywhere else
                prev=current.getPrevious()
                node=d_linked_node(item, current, current.getPrevious())
                prev.setNext(node)
                current.setPrevious(node)
                self.size+=1
        else:
            raise Exception("You can't insert at a position that doesn't exist") 
                
    def pop1(self):
        if self.head==None:#nothing in the list
            return None
        else:
            if self.head==self.tail:#one item in the list
                temp=self.head
                self.head=None
                self.tail=None
                self.size=0
                return temp.getData()
            else:#more than one item in the list
                node=self.tail
                node.getPrevious().setNext(None)
                self.tail=node.getPrevious()
                self.size-=1
                return node.getData()
        
    def pop(self, pos):
        current=self.head
        i=0
        if current==None:#nothing at the head, wont be able to pop any value
            return None        
        while current.getNext()!=None and i<pos:
            current=current.getNext()
            i+=1
        if i==pos:
            if pos==0 and current.getNext()==None:#position 0
                temp=self.head
                self.head=None
                self.tail=None  
                self.size=0
                return temp.getData()
            elif pos==0:
                self.head=current.getNext()
                self.size-=1
                return current.getData()                
            else:
                if current.getNext()==None:
                    current.getPrevious().setNext(current.getNext())
                    self.tail=current.getPrevious()
                    self.size-=1
                    return current.getData()
                else:
                    current.getPrevious().setNext(current.getNext())
                    current.getNext().setPrevious(current.getPrevious())
                    self.size-=1
                    return current.getData()
            
    def search_larger(self, item):
        current=self.head
        i=0
        if current.getData()>item:
            return i
        while current.getNext()!=None:
            current=current.getNext()
            i+=1
            if current.getData()>item:
                return i
        return -1
    
    def get_size(self):
        return self.size
    
    def get_item(self, pos):
        if self.head==None:
            raise Exception("There is no item at that position")        
        elif pos==0:
            return self.head.getData()
        elif pos>0:
            current=self.head
            i=0
            while i<pos and current.getNext()!=None:
                current=current.getNext()
                i+=1
            if i==pos:
                return current.getData()
            else:
                raise Exception("There is no item at that position") 
        else:#pos<0
            current=self.tail
            i=-1
            while i>pos and current.getPrevious()!=None:
                current=current.getPrevious()
                i-=1
            if i==pos:
                return current.getData()
            else:
                raise Exception("There is no item at that position") 
            
    def __str__(self):
        current=self.head
        if current!=None:
            string=str(current.getData())
        else:
            return "None"
        while current.getNext()!=None:
            string+=" "
            current=current.getNext()
            string+=str(current.getData())
        return string
            
def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
    
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop1() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                    
        
                    
    for i in range(0, 1000):
        int_list.append(i) 
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
                
    for i in range(0, 200):
        popped=int_list.pop1()
        if popped != 999 - i:
            correctOrder = False                       
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801) 
    
    print(int_list)
    print(int_list.search_larger(800))
      
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
        
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")
                
if __name__ == '__main__':
    test()
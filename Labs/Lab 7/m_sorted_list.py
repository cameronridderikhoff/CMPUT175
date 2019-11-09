from d_linked_list import d_linked_list
from d_linked_node import d_linked_node


class m_sorted_list:
    
    def __init__(self, m_sorted):
        self.mSorted=m_sorted
        self.items=d_linked_list()
        
    def add(self, item):
        if self.mSorted:
            if self.items.head==None:
                self.items.add(item)
            else:
                current=self.items.head
                i=0
                while current.getNext()!=None and current.getData()<item:
                    current=current.getNext()
                    i+=1
                #if we are the the end of the list, but the current node is still smaller, we add the item to the tail
                if current.getNext()==None and current.getData()<item:
                    self.items.append(item)
                #current is the tail, node goes right before it
                elif current.getNext()==None and current.getData()>=item:
                    if i>0:
                        self.items.insert(self.items.get_size()-1, item)
                    else:
                        self.items.insert(i, item)
                else:
                    self.items.insert(i, item)
        else:
            self.items.append(item)
                
        
    def pop(self):
        if self.mSorted:
            return self.items.pop1()
        else:
            return self.items.pop(0)
    def search(self, item):
        found=self.items.search(item)
        if not self.mSorted:
            if not found:
                return (found, -1)
            else:
                index=self.items.index(item)
                return (found, index)
        else:
            if not found:
                larger=self.items.search_larger(item) #will already return -1 if there is no larger item
                return (found, larger)
            else:
                index=self.items.index(item)
                return (found, index)
        
    def change_sorted(self):
        if self.mSorted:
            self.mSorted=False
        else:
            raise Exception("I don't know how to sort a doubly linked list yet")
        
    def get_size(self):
        return self.items.get_size()
        
    def get_item(self, pos):
        return self.items.get_item(pos)
        
    def __str__(self):
        return str(self.items)
        
def test():
                  
    sor_list = m_sorted_list(True)
                    
    is_pass = (sor_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    sor_list.add(4)
    sor_list.add(3)
    sor_list.add(8)
    sor_list.add(7)
    sor_list.add(1)
    
    is_pass = (str(sor_list) == "1 3 4 7 8")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list.get_size() == 5)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list.pop() == 8)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list.pop() == 7)
    assert is_pass == True, "fail the test"
    
    is_pass = (str(sor_list) == "1 3 4")
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == 1)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(3)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(7)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    is_pass = (sor_list.get_size() == 3)
    assert is_pass == True, "fail the test"  
    
    is_pass = (sor_list.get_item(2) == 4)
    assert is_pass == True, "fail the test"      
    
    sor_list.change_sorted()
    
    sor_list.add(1)
               
    is_pass = (str(sor_list) == "1 3 4 1")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"       
    
    is_pass = (sor_list.pop() == 1)
    assert is_pass == True, "fail the test"
       
      
    is_pass = (sor_list.pop() == 3)
    assert is_pass == True, "fail the test"
    
    sor_list.add(7)
    sor_list.add(6)
    
    is_pass = (str(sor_list) == "4 1 7 6")
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(7)
    is_pass = (a[0] == True and a[1] == 2)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(8)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"  
    
    is_pass = (sor_list.get_item(2) == 7)
    assert is_pass == True, "fail the test"      
      
    
    sor_list2 = m_sorted_list(False)
                    
    is_pass = (sor_list2.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    sor_list2.add(4)
    sor_list2.add(3)
    sor_list2.add(8)
    sor_list2.add(7)
    sor_list2.add(1)
               
    is_pass = (str(sor_list2) == "4 3 8 7 1")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 4)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 3)
    assert is_pass == True, "fail the test"
    
    is_pass = (str(sor_list2) == "8 7 1")
    assert is_pass == True, "fail the test"
    
    a = sor_list2.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    a = sor_list2.search(7)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"
    
    is_pass = (sor_list2.get_size() == 3)
    assert is_pass == True, "fail the test"  
    
    is_pass = (sor_list2.get_item(2) == 1)
    assert is_pass == True, "fail the test"      
    
    try:
        sor_list2.change_sorted()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"    
    
    
    sor_list2.add(3)
    sor_list2.add(2)
               
    is_pass = (str(sor_list2) == "8 7 1 3 2")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 8)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 7)
    assert is_pass == True, "fail the test"
    
    
    is_pass = (str(sor_list2) == "1 3 2")
    assert is_pass == True, "fail the test"
                  
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")
                
if __name__ == '__main__':
    test()

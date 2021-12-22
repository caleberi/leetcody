
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None  and self.tail  is None


    def insert_front(self,value):
        node =  Node(value) 
        if self.is_empty():
            self.head = self.tail =   node
        else:
            old_head = self.head
            node.next = old_head
            old_head.prev =  node
            self.head =  node
            
    def insert_back(self,value):
        node =  Node(value) 
        if self.is_empty():
            self.head = self.tail =   node
        else:
            old_tail = self.tail
            old_tail.next =  node
            self.tail = node
    
    def print_list(self):
        curr =  self.head
        while curr is not None:
            print(curr.value)
            curr =  curr.next

    
    

        
if __name__ == "__main__":
    l = List()
    l.insert_front(34)
    l.insert_back(90) 
    l.insert_back(50)  
    l.print_list()




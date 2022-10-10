

class Node:
    def __init__(self,val) -> None:
        self.val =  val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.len = 0

    def enqueue(self, val):
        if self.front is None:
            self.front = self.back =  Node(val)
        else:
            node = Node(val)
            self.back.next = node
            self.back = node
        self.len += 1

    def isEmpty(self)->bool:
        return self.len == 0
            
    def dequeue(self)-> bool:
        if self.isEmpty():
            return False
        nodeTodelete = self.front
        self.front = self.front.next
        nodeTodelete.next = None
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def getBack(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.val



class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = Queue()
        self.__max = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        self.queue.enqueue(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): 
            return False
        return self.queue.dequeue()

    def Front(self) -> int:
        return self.queue.getFront()

    def Rear(self) -> int:
        return self.queue.getBack()
        

    def isEmpty(self) -> bool:
        return self.queue.isEmpty()
        

    def isFull(self) -> bool:
        return self.queue.len == self.__max
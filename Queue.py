class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x)
            self.tail.next = node
            self.tail = node

    def pop(self) -> int:
        node = self.head
        self.head = self.head.next
        node.next = None
        return node.info

    def peek(self) -> int:
        return self.head.info

    def empty(self) -> bool:
        return True if self.head is None else False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

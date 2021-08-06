class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
            self.length += 1
        else:
            node = Node(x)
            node.prev = self.tail
            if self.tail and self.tail.next:
                self.tail.next = node
            self.tail = node
            self.length += 1

    def pop(self) -> int:
        tailToBeRemoved = self.tail
        tailToBe = self.tail.prev
        self.tail = tailToBe
        if self.tail is not None:
            self.tail.next = None
        self.length -= 1
        return tailToBeRemoved.info

    def top(self) -> int:
        return self.tail.info

    def empty(self) -> bool:
        return self.length == 0

class Person:
    def __init__(self, name):
        self.name = name
        self.next = None


class BankQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, name):
        if self.head is None:
            self.head = Person(name)
            self.tail = self.head
        else:
            node = Person(name)
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        node = self.head # reference to the current person at the extreme front
        self.head = self.head.next
        node.next = None
        return node.name

    def firstPersonInTheQueue(self):
        return self.head.name

    def lastPersonInTheQueue(self):
        return self.tail.name


    def empty(self):
        return True if self.head is None else False


queue = BankQueue()
queue.enqueue("Wole")
queue.enqueue("Bola")
queue.enqueue("Victor")
queue.enqueue("Paul")
queue.enqueue("Mustafa")

print(queue.dequeue())
print(queue.firstPersonInTheQueue())
print(queue.dequeue())
print(queue.empty())
print(queue.firstPersonInTheQueue())
print(queue.lastPersonInTheQueue())

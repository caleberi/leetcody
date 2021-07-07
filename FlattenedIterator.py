class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def hasNext(self):
        return self.next is not None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if self.empty():
            self.head = self.tail = QNode(value)
        else:
            node = QNode(value)
            self.tail.next = node
            self.tail = node

    def get(self):
        if self.empty():
            return None
        else:
            currentHead = self.head
            if currentHead is None:
                newHead = None
                self.head = newHead
                return currentHead
            newHead = currentHead.next
            self.head = newHead
            return currentHead

    def top(self):
        return self.head.data if self.head is not None else None

    def empty(self):
        return self.head is None and self.tail is None


class Iterator:
    def __init__(self, input):
        self.queue = Queue()
        if hasattr(input, '__len__'):
            for data in input:
                self.queue.put(data)
        else:
            self.queue.put(input)

    def qqueue(self):
        return self.queue


class FlattenedIterator:
    def __init__(self, subiterators):
        self.iteratorQueue = Queue()
        for iterator in subiterators:
            self.iteratorQueue.put(Iterator(iterator))

    def hasNext(self):
        return not self.iteratorQueue.top().qqueue().empty()

    def next(self):
        if self.hasNext():
            itr_queue = self.iteratorQueue.get().data
            queue = itr_queue.qqueue()
            val = queue.get()
            if not queue.empty():
                if val and isinstance(val.data, list):
                    self.iteratorQueue.put(Iterator(val))
                else:
                    self.iteratorQueue.put(itr_queue)
                    if val and val.data is not None:
                        return val.data
        else:
            return None


class EmptyIterator:
    def __init__(self, name):
        self.name = name

    def hasNext(self):
        return False

    def next(self):
        raise Exception()


# it = FlattenedIterator([EmptyIterator("1"), EmptyIterator("3")])
# assert(not it.hasNext())
# print(it.hasNext())
# print(it.next().name)
# print(it.next().name)

it = FlattenedIterator([[1, 2, 4, 6], [7, 8, 9], [10, 11, [90]]])
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())
print(it.next())

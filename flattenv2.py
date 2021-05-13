# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self, value):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

# User defined class


class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    def popFront(self):
        if self.head is None:
            return
        self.head = self.head.next

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:       # <-- Iterate untill we have nodes available
            # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            out.append(int(str(node.value)))
            node = node.next

        return out


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    result = LinkedList(-100)
    pointerOne, pointerTwo = list1.head, list2.head
    while pointerOne and pointerTwo:
        if pointerOne.value <= pointerTwo.value:
            result.append(pointerOne.value)
            pointerOne = pointerOne.next
        if pointerOne.value >= pointerTwo.value:
            result.append(pointerTwo.value)
            pointerTwo = pointerTwo.next
    if pointerOne and pointerTwo is None:
        while pointerOne:
            result.append(pointerOne.value)
            pointerOne = pointerOne.next
    if pointerTwo and pointerOne is None:
        while pointerTwo:
            result.append(pointerTwo.value)
            pointerTwo = pointerTwo.next
    result.popFront()
    return result


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        def flattenList(node):
            if node.next is None:
                return merge(node.value, None)
            return merge(node.value, flattenList(node.next))
        return flattenList(self.head)

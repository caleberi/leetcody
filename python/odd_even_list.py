

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        oddLinkedListHead, oddLinkedListTail = generateLinkedListBasedOnParity(
            head, odd)
        evenLinkedListHead, evenLinkedListTail = generateLinkedListBasedOnParity(
            head, even)
        oddLinkedListTail.next = evenLinkedListHead
        evenLinkedListTail.next = None
        return oddLinkedListHead


def odd(val):
    return True if val % 2 == 1 else False


def even(val):
    return True if val % 2 == 0 else False


def generateLinkedListBasedOnParity(head, func):
    pointer = head
    result = None
    presult = None
    i=1
    while pointer is not None:
        if func(i):
            if result is None:
                result = ListNode(pointer.val)
                presult = result
            else:
                presult.next = ListNode(pointer.val)
                presult = presult.next
        i+=1
        pointer = pointer.next
    return (result, presult)

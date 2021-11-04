# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        return nodeSwap(head)


def nodeSwap(head):
    if head and head.next is None:
        return head

    count = 1
    prev = None
    current = head
    newHead = None
    while current.next is not None:
        if count % 2 == 0:
            if newHead is None:
                newHead = current
            # swapNode(prev, current)
            temp = current.next
            current.next = prev
            prev.next = temp
        count += 1
        prev = current
        current = current.next
    return newHead

    # 1->3->4


# def swapNode(prev, current):
#     temp = current
#     current.next = prev
#     prev.next = temp.next

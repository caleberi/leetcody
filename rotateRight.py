# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        n = 1
        listTail = head
        while listTail.next is not None:
            listTail = listTail.next
            n += 1
        offset = abs(k) % n
        if offset == 0:
            return head
        newTailPosition = n-offset if k > 0 else offset
        newTail = head
        for i in range(1, newTailPosition):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        listTail.next = head
        return newHead

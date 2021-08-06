# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        current = head
        while current is not None:
            if current.next and current.next.val == val:
                nodeToDelete = current.next
                current.next = current.next.next
                nodeToDelete.next = None
            else:
                current = current.next
        return head

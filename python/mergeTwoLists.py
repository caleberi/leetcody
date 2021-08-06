# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        ret = None
        pret = None
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                if ret is None:
                    ret = p1
                    pret = ret
                    p1 = p1.next
                else:
                    pret.next = p1
                    pret = pret.next
                    p1 = p1.next
            elif p2.val <= p1.val:
                if ret is None:
                    ret = p2
                    pret = ret
                    p2 = p2.next
                else:
                    pret.next = p2
                    pret = pret.next
                    p2 = p2.next
        if p1 and p2 is None:
            while p1 is not None:
                if ret is None:
                    ret = p1
                    pret = ret
                    p1 = p1.next
                else:
                    pret.next = p1
                    pret = pret.next
                    p1 = p1.next

        if p2 and p1 is None:
            while p2 is not None:
                if ret is None:
                    ret = p2
                    pret = ret
                    p2 = p2.next
                else:
                    pret.next = p2
                    pret = pret.next
                    p2 = p2.next

        return ret

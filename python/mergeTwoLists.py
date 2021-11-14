from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l2 is None and l1 is not None:
            return l1

        ret = ListNode(-1)
        curr = ret
        while l1 is not None and l2 is not None :
            if l1.val >= l2.val:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                curr = curr.next
            else:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                curr = curr.next
                
        while l1 is not None and l2 is None:
            curr.next = ListNode(l1.val)
            l1 = l1.next
            curr = curr.next

        while l2 is not None and l1 is  None:
            curr.next = ListNode(l2.val)
            l2 = l2.next
            curr = curr.next
        return ret.next

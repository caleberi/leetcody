# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head=None
            return head
        count=1
        curr=head
        while curr.next:
            count+=1
            curr=curr.next
        n=count-n
        if n==0:
            f=head
            head=head.next
            f=None
            return head
        m=head
        i=1
        while i<n:
            m=m.next
            i+=1
        nodetodelete=m.next
        after=None
        if m.next is not None:
            after = m.next.next
        m.next=after
        nodetodelete=None
        return head
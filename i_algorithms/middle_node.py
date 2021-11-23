# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_length(node):
            length=0
            curr = node
            while curr is not None:
                length+=1
                curr = curr.next
            return length
        
        def middle_node(node,midIdx):
            if node is None:
                return node
            idx=0
            curr = node
            while idx!=midIdx:
                idx+=1
                curr=curr.next
            return curr
        length = get_length(head)
        if length <=1:
            return head
        if length%2==1:
            return middle_node(head,length//2)
        else:
            return middle_node(head,length/2)
        
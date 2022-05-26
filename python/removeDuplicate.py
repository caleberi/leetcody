from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nextNode,currentNode = head.next,ListNode(head.val)
        ret = currentNode
        while nextNode is not None:
            if currentNode.val != nextNode.val:
                currentNode.next = ListNode(nextNode.val)
                currentNode = currentNode.next
            nextNode = nextNode.next
        return ret
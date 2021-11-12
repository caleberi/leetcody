from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = self.remove_elements_helper(head,val)
        if prev and prev.val == val:
            node_to_remove = prev
            new_after_node = prev.next
            head = new_after_node
            node_to_remove.next = None
        return head
    
    def remove_elements_helper(self,head,val):
        if head is None:
            return None
        prev = self.remove_elements_helper(head.next,val)
        if prev and prev.val == val:
            node_to_remove = prev
            new_after_node = prev.next
            head.next = new_after_node
            node_to_remove.next = None
        return  head

            

# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        if not len(lists):
            return None

        while len(lists) > 1:
            newLists = []
            for i in range(0, len(lists), 2):
                LL1 = lists[i]
                LL2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList = self.merge(LL1, LL2)
                newLists.append(mergedList)
            lists = newLists
        return lists[0]

    def merge(self, list_1: ListNode, list_2: ListNode):
        if list_1 is None and list_2 is None:
            return None
        if list_1 is None and list_2:
            return list_2
        if list_2 is None and list_1:
            return list_1

        dummy = ListNode()
        ptr = dummy
        while list_1 is not None and list_2 is not None:
            if list_1.val >= list_2.val:
                ptr.next = ListNode(list_2.val)
                ptr = ptr.next
                list_2 = list_2.next
            else:
                ptr.next = ListNode(list_1.val)
                ptr = ptr.next
                list_1 = list_1.next

        if list_1 is not None and list_2 is None:
            ptr.next = list_1

        if list_2 is not None and list_1 is None:
            ptr.next = list_2

        return dummy.next

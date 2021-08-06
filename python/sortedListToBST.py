class ListNode(object):
    """ Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):

        def buildTree(i, j):
            if i > j:
                return None
            mid, node = (i+j)//2, TreeNode()
            node.left = buildTree(i, mid)
            node.val, curr[0] = curr[0].val, curr[0].next
            node.right = buildTree(mid+1, j)
            return node

        curr, count = head, 0
        while curr:
            curr = curr.next
            count += 1
        curr = [head]
        return buildTree(0, count)



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: "TreeNode"):
        def isLeaf(node):
            return node.left is None and node.right is None
        if root is None:
            return 0
        q = [root]
        s = 0
        while len(q):
            curr = q.pop()
            if curr.left is not None:
                if isLeaf(curr.left):
                    s += curr.left.val
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        return s

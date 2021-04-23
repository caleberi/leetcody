class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        vector = []
        self.inorderTraversalHelper(root, vector)
        return vector

    def inorderTraversalHelper(self, node, vector):
        if node is None:
            return
        if node.left:
            self.inorderTraversalHelper(node.left, vector)
        vector.append(node.val)
        if node.right:
            self.inorderTraversalHelper(node.right, vector)

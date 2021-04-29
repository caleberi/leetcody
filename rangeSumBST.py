class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         total = 0
#         total += self.rangeSumBSTHelper(root, low, high, total)
#         return total

#     def rangeSumBSTHelper(self, node, low, high, total):
#         if node is None:
#             return 0
#         left = self.rangeSumBSTHelper(node.left, low, high, total)
#         right = self.rangeSumBSTHelper(node.right, low, high, total)
#         if node.val >= low and node.val <= high:
#             total += node.val
#         return left+right+total


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        total += self.rangeSumBSTHelper(root, low, high, total)
        return total

    def rangeSumBSTHelper(self, node, low, high, total):
        if node is None:
            return 0
        left = self.rangeSumBSTHelper(node.left, low, high, total)
        right = self.rangeSumBSTHelper(node.right, low, high, total)
        if low <= node.val <= high:
            total += node.val
        return left+right+total

        

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def dfs(node, min_=float("-inf"), max_=float("inf")):
            if node is None:
                return True
            if node.val > max_ or node.val < min_:
                return False
            if dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_):
                return True
            return False
        return dfs(root)

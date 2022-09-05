from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree:TreeNode,min_t=float("inf"),max_t=float("-inf")):
            if tree is None:
                return
            pass

        # find the minimum possible height of the tree
        # find the maximum possible height of the tree
        
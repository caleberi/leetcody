from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDepthHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if not root.left :
            return self.minDepthHelper(root.right) + 1 
        if not root.right :
            return self.minDepthHelper(root.left) + 1
        left = self.minDepthHelper(root.left)
        right = self.minDepthHelper(root.right)
        
        return min(left,right)+1


    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.minDepthHelper(root)
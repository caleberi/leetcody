
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return hasPathSum(root,targetSum)

def hasPathSum(root, targetSum):
    if root is None :
        return False
    return hasPathSumHelper(root,targetSum,0)

def is_leaf(node):
    return node and node.left is None and node.right  is None

def hasPathSumHelper(root,targetSum,currentSum):
    if root:
        if is_leaf(root) :
            currentSum+=root.val
            return True if currentSum == targetSum else False
        left = hasPathSumHelper(root.left,targetSum ,currentSum+root.val)
        right = hasPathSumHelper(root.right,targetSum,currentSum+root.val)
        return left or right
    return False
    
    
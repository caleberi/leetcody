from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode],root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is  None and root2 is not None:
            return root2
        
        if root2 is  None and root1 is not None:
            return root1
        
        root = None
        if root1 is not None and root2 is not None:
            if root2.val >= root1.val:
                root = root2
                other = root1
                self.mergeTreeHelper(root,other)
            elif root1.val > root2.val:
                root = root1
                other = root2
                self.mergeTreeHelper(root,other)
        return  root
    
    def mergeTreeHelper(self,tree,other):
        if tree is  None and other is  None:
            return
            
        if tree is not None and other is not None:
            new_value = tree.val+other.val
            tree.val = new_value
            self.mergeTreeHelper(tree.left,other.left)
            self.mergeTreeHelper(tree.right,other.right)

        if tree and tree.left is None and other and other.left is not None:
            tree.left = other.left
            
            
        if tree and tree.right is None and other and other.right is not None:
            tree.right = other.right
            
        
        
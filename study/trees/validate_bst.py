from typing import Optional

from study.trees.deserialize_serialize_tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root)
    
    def isValidBSTHelper(self,root,minValue=float('-inf'),maxValue=float('inf')):
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue :
            return False
        return self.isValidBSTHelper(root.left,minValue,root.val) and \
        self.isValidBSTHelper(root.right,root.val,maxValue)
        
            
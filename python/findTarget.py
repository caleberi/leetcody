from typing import Optional

# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        def dfs(root,m,target):
            if root is None:
                return 
            if root.val not in m:
                m[root.val] = root
            if root.left:
                dfs(root.left,m,target)
            if root.right:
                dfs(root.right,m,target)
        if root and root.left is None and root.right is None:
            return False
        m = {}
        dfs(root,m,target)
        for k,v in m.items():
            dif = target-k
            if dif in m and m[dif] != m[k]:
                return True
        return False


        
        
            
            
                
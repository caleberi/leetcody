from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare_tree(node_a:TreeNode,node_b:TreeNode)->bool:
            if node_a is None and node_b is None:
                return True
            if (node_a is None and node_b is not None) or (node_b is None and node_a is not None):
                return False
            
            left_child = compare_tree(node_a.left,node_b.left)
            right_child = compare_tree(node_a.right,node_b.right)
            
            if node_a.val != node_b.val:
                return False
            return left_child and right_child
        
        def dfs(tree:TreeNode,sub_root:TreeNode):
            if tree is None:
                return False
            
            left_child = dfs(tree.left,sub_root)
            right_child = dfs(tree.right,sub_root)
            
            ret = False
            if tree.val == sub_root.val:
                ret = ret or compare_tree(tree,sub_root)
            if ret:
                return ret
            return left_child or right_child
        
        return dfs(root,subRoot)
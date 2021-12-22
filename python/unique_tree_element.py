class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        def insert_in_root(root,new_node):
            if root is None :
                return
            if new_node.val < root.val  and root.left is not None:
                if root.left is None:
                    root.left = new_node
                return insert_in_root(root.left,new_node)
            if new_node.val > root.val and root.right is not None:
                if root.right is None:
                    root.right = new_node
                return insert_in_root(root.right,new_node)
            return False
        
        possible_tree_elements =  [i for i in range(1,n)]
        for i in range(len(possible_tree_elements)):
            root = TreeNode(possible_tree_elements[i])
            insert_in_root(root,self.generateTrees())

            
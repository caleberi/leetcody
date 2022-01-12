class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    if root:
        if root.val > val:
            if root.left:
                insertIntoBST(root.left, val)
            root.left = TreeNode(val)
            return
        elif root.val < val:
            if root.left:
                insertIntoBST(root.right, val)
            root.right = TreeNode(val)
            return
    return TreeNode(val)

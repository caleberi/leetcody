# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def swap(node):
            temp = node.left
            node.left = node.right
            node.right = temp

        if root is None:
            return root
        queue = [root]
        while len(queue):
            node = queue.pop()
            swap(node)
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return root

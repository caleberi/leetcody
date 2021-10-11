# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        nodes = []
        trees = getPresentTrees(root, nodes)
        trees.append(None)
        for idx, tree in enumerate(nodes):
            if idx+1 < len(trees):
                tree.right = nodes[idx+1]
                tree.left = None
        return trees[0]


def getPresentTrees(node, vector):
    if node is None:
        return
    vector.append(node)
    getPresentTrees(node.left, vector)
    getPresentTrees(node.right, vector)
    return vector

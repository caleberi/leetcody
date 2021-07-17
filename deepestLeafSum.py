
# class Detail:
#     """
#     parameters:
#         sum - tracks the sum of deepestLeaf \n
#         depth -  tracks the depth of tree \n
#         max_depth - tracks the maximum depth obtained from traversing the tree
#     """

#     def __init__(self, sum, depth, max_depth):
#         self.sum = sum
#         self.depth = depth
#         self.max_depth = max_depth


# def isLeaf(node):
#     return node and node.left is None and node.right is None


# def deepestLeafSum(node):
#     detail = Detail(0, 1, 0)
#     deepestLeafSumHelper(node, detail)
#     return detail.sum


# def deepestLeafSumHelper(node, detail):
#     if node is not None and isLeaf(node) and detail.depth >= detail.max_depth:
#         detail.sum += node.value
#         detail.max_depth = detail.depth
#         detail.depth -= 1
#         return detail
#     if node and node.left:
#         if detail.depth >= detail.max_depth:
#             detail.max_depth = detail.depth
#         detail.depth += 1
#         deepestLeafSumHelper(node.left, detail)
#         detail.depth -= 1
#         detail.node = node
#     if node and node.right:
#         if detail.depth >= detail.max_depth:
#             detail.max_depth = detail.depth
#         detail.depth += 1
#         deepestLeafSumHelper(node.right, detail)
#         detail.depth -= 1
#         detail.node = node
#     return detail


"""
        [1]                
        /  \
     [2]    [3]
     / \       \ 
   [4] [5]     [6]
   /              \
 [7]               [8]

[1,{0,1,0}] [1,{15,1,4}]
[2,{0,2,1}] [2,{7,2,4}] [2,{7,2,4}] [3,{7,2,4}] [3,{15,2,4}]
[4,{0,3,2}] [4,{7,3,4}] [5,{7,3,4}]  [6,{7,3,4}] [6,{15,3,4}]
[7,{7,4,3}] [8,{7+8,4,4}]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return deepestLeaf(root)


def deepestLeaf(node):
    if node is None:
        return 0
    queue = [(node, 1)]
    max_depth = 1
    sum = node.val
    while queue:
        current = queue.pop(0)
        currentNode = current[0]
        currentLevel = current[1]
        if currentLevel > max_depth and isLeaf(currentNode):
            max_depth = currentLevel
            sum = currentNode.val
        elif currentLevel == max_depth and isLeaf(currentNode):
            # print("sum : ",sum)
            # print("******************")
            # print("currentNode: " , currentNode.val)
            # print("currentLevel: ", currentLevel)
            # print("******************")
            sum += currentNode.val
        if currentNode and currentNode.left:
            queue.append((currentNode.left, currentLevel+1))
        if currentNode and currentNode.right:
            queue.append((currentNode.right, currentLevel+1))
    return sum


def isLeaf(node):
    return node and node.left is None and node.right is None

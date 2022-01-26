# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list_one = get_element_in_tree(root1, [])
        list_two = get_element_in_tree(root2, [])
        list_one.sort()
        list_two.sort()
        return merge(list_one, list_two)


def get_element_in_tree(tree, result):
    if tree is None:
        return result
    result.append(tree.val)
    result = get_element_in_tree(tree.left, result)
    result = get_element_in_tree(tree.right, result)
    return result


def merge(l1, l2, result=[]):
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        elif l2[j] <= l1[i]:
            result.append(l2[j])
            j += 1
    while i < len(l1):
        result.append(l1[i])
        i += 1
    while j < len(l2):
        result.append(l2[j])
        j += 1
    return result

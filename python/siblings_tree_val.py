"""
https://binarysearch.com/problems/Sibling-Tree-Value
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root, k):
        parent_map = {root.val:None}
        queue = [root]
        while len(queue) and k not in parent_map:
            curr_root = queue.pop(0)
            if curr_root and curr_root.left is not None:
                if curr_root.left.val not in parent_map:
                        parent_map[curr_root.left.val]=[curr_root]
                        queue.append(curr_root.left)
                else:
                    parent_map[curr_root.left.val].append(curr_root)
                    queue.append(curr_root.left)
            if curr_root and curr_root.right is not None:
                if curr_root.right.val not in parent_map:
                        parent_map[curr_root.right.val]=[curr_root]
                        queue.append(curr_root.right)
                else:
                    parent_map[curr_root.right.val].append(curr_root)
                    queue.append(curr_root.right)
        if k < parent_map[k][0].val:
            if parent_map[k][0].right is not None:
                return parent_map[k][0].right.val
            return None
        else:
            if parent_map[k][0].left is not None:
                return parent_map[k][0].left.val
            return None
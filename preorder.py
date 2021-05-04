"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node', queue=[]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        ret = []
        while len(queue):
            ret.append(queue[0].val)
            for node in queue[0].children:
                ret.extend(self.preorder(node, queue))
            queue.pop(0)
        return ret

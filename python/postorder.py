"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if root is None:
            return ret
        level = [root]
        while level:
            node = level.pop()
            ret.append(node.val)
            for kid in node.children:
                level.append(kid)
        ret.reverse()
        return ret

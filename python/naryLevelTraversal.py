
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        result = []
        while queue:
            ret =  []
            l_queue = len(queue)
            while l_queue:
                curr = queue.popleft()
                ret.append(curr)
                if curr.children:
                    for child in curr.children:
                        queue.append(child)
                l_queue-=1
            result.append(ret)
        return result

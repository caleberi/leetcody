from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next




class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        dq = deque([root])
        while dq:
            size = len(dq)
            csize = size
            for _ in range(size):
                current = dq.popleft()
                if current.left:
                    dq.append(current.left)
                if current.right:
                    dq.append(current.right)
                size -= 1
            csize = len(dq)
            if csize > 1:
                ldq = list(dq);
                for i in range(csize-1):
                    ldq[i].next = ldq[i+1]
        return root
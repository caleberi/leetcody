# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
from math import pow


class Solution:
    def solve(self, node):
        def dfs(node):
            if node is None:
                return (0, 0)
            total = 0
            val, exp = dfs(node.next)
            total += node.val*pow(2, exp)+val
            return (total, exp+1)
        ans, exp = dfs(node)
        return ans

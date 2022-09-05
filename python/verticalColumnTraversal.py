from collections import defaultdict
from typing import Dict, List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(tree: Optional[TreeNode],pos:tuple):
            if tree:
                ans.append((pos[0],pos[1],tree.val))
                dfs(tree.left,(pos[0]-1,pos[1]+1))
                dfs(tree.right,(pos[0]+1,pos[1]+1))
        
        dfs(root,(0,0))
        ans.sort(key= lambda v : (v[0],v[1],v[2]))
        d=defaultdict(list)
        for i,j,k in ans:
            d[i].append(k)
        l=[]
        for i in d.values():
            l.append(i)
        return l
        
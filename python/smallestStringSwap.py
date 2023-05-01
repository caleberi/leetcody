from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        l = len(s)
        uf = UnionFind(l)
        for pair in pairs:
            uf.union(pair[0],pair[1])
        groups = uf.getGroups()
        print(groups)
        res = ['-'] * l
        for group in groups:
            chars = [s[i] for i in group]
            chars.sort()
            group.sort()
            for i, c in zip(group, chars):
                res[i] = c
        return "".join(res)
            
            
        

class UnionFind:
    def __init__(self, length):
        self.size = length
        self.root = [i for  i in range(length)]
        self.rank = [1] * length
            
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def union(self, x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def getGroups(self):
        groups = defaultdict(list)
        for u in range(self.size):
            groups[self.find(u)].append(u)
        return groups.values()
                
        
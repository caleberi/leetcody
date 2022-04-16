from math import sqrt
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h_d = {}
        for i in range(len(points)):
            d = self.distance(points[i])
            if d not in h_d:
                h_d[d] = [points[i]]
            else:
                h_d[d].append(points[i])
        keys = list(h_d.keys())
        keys.sort()
        ret = []
        for i in range(k):
            if len(ret) < k:
                ret.extend(h_d[keys[i]])
        return ret[:k]
        
    def distance(self,point):
        x = point[0]*point[0]
        y = point[1]*point[1]
        return sqrt(x+y)
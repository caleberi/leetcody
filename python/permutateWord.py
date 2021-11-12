    
from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        l = len(s1)
        ls1=list(s1)
        ls2 =list(s2)
        freq = Counter(ls1)
        for i in range(len(s2)):
            freq_from_ith = Counter(ls2[i:i+l])
            if freq == freq_from_ith:
                return True
        return False
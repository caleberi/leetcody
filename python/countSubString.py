from collections import Counter


class Solution:
    def countSubstrings(self, s: str) -> int:
        if self.all_characters_are_unique(s): #O(N)
            return len(s)
        
        
        

    def all_characters_are_unique(self,s)->bool:
        c = Counter(s)
        for _,v in c.items():
            if v > 1:
                return False
        return True
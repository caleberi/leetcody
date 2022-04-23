# 120 / 120 test cases passed.
# Status: Accepted
# Runtime: 50 ms
# Memory Usage: 13.9 MB

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = { ch : i for (i,ch) in enumerate(order) }
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            for j in range(len(w1)):
                if j==len(w2):
                    return False
                if w1[j] != w2[j] :
                    if table[w2[j]] < table[w1[j]] : 
                        return False  
                    break
        return True


        
if __name__ == "__main__":
    s = Solution()
    print(s.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))
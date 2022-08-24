from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1 :
            return False
        if n == 1 :
            return True
        return self.isPowerOfThree(n/3)
    
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
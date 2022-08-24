from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1 :
            return False
        if n == 1 :
            return True
        return self.isPowerOfThree(n/3)
    
    def isPowerOfThree(self, n: int) -> bool:
        # Any integer number other than power of 3 which divides 
        # highest power of 3 value that integer can hold 3^19 = 1162261467 
        # (Assuming that integers are stored using 32 bits) will give reminder non-zero.
        return n > 0 and 1162261467 % n == 0
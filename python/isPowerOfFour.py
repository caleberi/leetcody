from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfFour(n/4)
    
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not ( n & (n-1)) and int(sqrt(n)) * int(sqrt(n)) == n
    
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not ( n & (n-1)) and n & 1431655765 == n
    
    def isPowerOfFour(self, n: int)  -> bool:
        return n > 0 and log(n, 4).is_integer()
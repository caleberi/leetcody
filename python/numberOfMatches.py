class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = -1
        advance = -1
        total = 0
        while n > 1:
            if n % 2 == 1:
                matches = (n-1)//2
                advance = ((n-1)//2)+1
                total += matches
                n = advance
                continue
            else:
                matches = (n)//2
                advance = (n)//2
                total += matches
                n = advance
                continue
        return total

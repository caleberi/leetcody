class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = numSquareSum(n)
        return True


def numSquareSum(n: int) -> int:
    digitSumSquare = 0
    while n:
        digitSumSquare += (n % 10)*(n % 10)
        n = int(n/10)
    return digitSumSquare

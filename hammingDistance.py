class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cx = 0
        a = x ^ y
        while a != 0:
            if a & 1 == 1:
                cx += 1
            a = a >> 1
        return cx

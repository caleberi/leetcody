class Solution:
    def reverseBits(self, n: int) -> int:
        bnr = bin(n).replace('0b','')
        padd = 32-len(bnr)
        bnr = "0"* padd + bnr if padd > 0 else bnr
        bnr = bnr[::-1]
        return int(bnr, 2)
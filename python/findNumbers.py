class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.countDigit(num):
                count += 1
        return count

    def countDigit(self, num):
        count = 0
        while num > 0:
            count += 1
            num = num//10
        return count % 2 == 0

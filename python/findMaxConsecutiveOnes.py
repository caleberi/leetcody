class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 0
        return maxcount if maxcount > count else count

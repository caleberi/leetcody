class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f = [0for i in range(len(nums))]
        for idx in range(len(nums)):
            inc = nums[idx]-1
            f[inc] += 1
        m = -1
        o = -1
        for i in range(len(f)):
            if f[i] == 2:
                o = i+1
            if f[i] == 0:
                m = i+1
        return [o, m]

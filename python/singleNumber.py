class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        lone = [nums[0]]
        for idx in range(1, len(nums)):
            if len(lone) == 0:
                lone.append(nums[idx])
            elif lone[-1] != nums[idx]:
                lone.append(nums[idx])
            else:
                lone.pop()
        return lone[0]

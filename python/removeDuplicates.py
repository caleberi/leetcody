class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        while idx < len(nums):
            if nums[idx-1] == nums[idx]:
                del nums[idx-1]
                idx -= 1
            idx += 1
        return len(nums)

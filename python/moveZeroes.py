class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonZeroPointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroPointer] = nums[i]
                nonZeroPointer += 1
        for i in range(nonZeroPointer, len(nums)):
            nums[i] = 0

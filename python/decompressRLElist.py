class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for idx in range(0, len(nums), 2):
            count = nums[idx]
            val = nums[idx+1]
            ret += [val for _ in range(count)]
        return ret

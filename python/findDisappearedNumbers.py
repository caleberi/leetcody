class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        l = []
        counter = [0 for _ in range(len(nums))]
        for n in nums:
            if counter[n-1] == 0:
                counter[n-1] = n
        for idx in range(len(counter)):
            if counter[idx] == 0:
                l.append(idx+1)
        return l

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not len(nums):
            return nums
        l = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            n = nums[i]
            l[n]= 1
        r = []
        for i in range(1,len(l)):
            if l[i]==0:
                r.append(i)
        return r
        

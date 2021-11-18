class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not len(nums):
            return nums
        l = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            n = nums[i]
            if l[n]==0:
                l[n]= 1
            else:
                l[n]+=1
        r = []
        for i in range(1,len(l)):
            if l[i]>1:
                r.append(i)
        return r
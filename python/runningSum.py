class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


# class Solution(object):
#     def runningSum(self, n):
#         i=1
#         l=len(n)
#         while i < l:
#             n[i]+=n[i-1]
#             i+=1
#         return n

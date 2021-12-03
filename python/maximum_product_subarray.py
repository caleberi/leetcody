class Solution:
    def maxProduct(self, nums):
        max_p = nums[0]
        for i in range(len(nums)):
            p = nums[i]
            for j in range(i+1,len(nums)):
                p *= nums[j]
                if p>max_p:
                    max_p = p
            if nums[i] >max_p:
                max_p = nums[i]
        return max_p
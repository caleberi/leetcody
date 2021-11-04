
"""
Given a list of positive integers nums, return the largest positive integer 
that divides each of the integers.
Constraints
    1 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [6, 12, 9]
output = 3
"""

class Solution:
    def solve(self, nums):
        # def gcd(a,b):
        #     if b == 0:
        #         return a
        #     return gcd(b,a%b)
        def gcd(a,b):
            while b != 0:
                t = b
                b = a % b
                a = t
            return a
       
        while len(nums)>1:
            x = nums.pop()
            y = nums.pop()
            nums.append(gcd(x,y))
        return nums[0]
"""
Given an integer n, return whether it is equal to 
the sum of its own digits raised to the power of the number of digits.
"""
class Solution:
    def solve(self, n):
        def digit_count(num):
            d=0
            while num>0:
                num=num//10
                d+=1
            return d
            
        def digit_power_sum(num):
            dc = digit_count(num)
            s = 0
            while num>0:
                rem = num%10
                num=num//10
                s+=rem**dc
            return s
        return digit_power_sum(n)==n
        
"""
Given a positive integer n, sum all of its digits to get a new number.
Repeat this operation until the new number is less than 10 and return it.
"""
class Solution:
    def solve(self, n):
        def sum_digit(n):
            if n < 10:
                return n
            s = 0
            while n>0:
                rm = n%10
                n = n // 10
                s+=rm
            return sum_digit(s)
        return sum_digit(n)
                
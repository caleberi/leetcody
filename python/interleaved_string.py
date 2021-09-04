"""
Given two strings s0 and s1, return the two strings interleaved,
starting with s0. 
If there are leftover characters in a string they should be added to the end.

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where n is the length of s1

Example
s0 = "abc"
s1 = "xyz"

returns "axbycz"
"""
class Solution:
    def solve(self, s0, s1):
        result = ""
        i = 0
        j = 0
        while i < len(s0) and j < len(s1):
            if i==j :
                result+=s0[i]
                i+=1
                continue
            result+=s1[j]
            j+=1
        while i < len(s0):
            result+=s0[i]
            i+=1
        while j < len(s1):
            result+=s1[j]
            j+=1
        return result
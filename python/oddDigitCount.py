class Solution:
    def solve(self, nums):
        return method_two(nums)

def method_one(nums):
    def has_odd_number_digit(n):
            d=0
            while n>0:
                n=n//10
                d+=1
            return d%2!=0
    cnt = 0
    for n in nums:
        if has_odd_number_digit(n):
            cnt+=1
    return cnt

def method_two(nums):
    cnt=0
    for n in nums:
        if len(str(n))%2!=0:
            cnt+=1
    return cnt
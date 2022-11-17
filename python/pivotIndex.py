from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # all integer array where all sums to the left are
        # equal to all sum to the right 
        # edge case :  if idx is a the oth pos then the sum = 0  ans = -1
        #    same for [n-1]th position
        # [1,7,3,6,5,6] = [1,8,11,17,22,28]
        # [1,7,3,6,5,6] = [28,27,20,17,11,6]
        # [1,2,3] = [1,3,6]
        #[1,2,3] = [6,5,3]
        a = nums[::]
        b = nums[::]
        for i in range(1,len(a)):
            a[i]=a[i-1]+a[i]
        for i in range(len(b)-2,-1,-1):
            b[i]=b[i+1]+b[i]
            
        for i in range(len(nums)):
            if a[i] == b[i]:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(s.pivotIndex([1, 2, 3]))
    print(s.pivotIndex([2, 1, -1]))
    print(s.pivotIndex([-1,-1,0,0,-1,-1]))
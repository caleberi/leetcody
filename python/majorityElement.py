from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ll = len(nums)
        ht = {}
        max_ = (-1,-1)
        for num in nums:
            if num not in ht:
                ht[num]=1
            else:
                ht[num]+=1
            if ht[num] > max_[1] and  ht[num] > ll//2:
                max_ = (num,ht[num])
                break
        return max_[0]


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))
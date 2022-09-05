from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        left,right =  0 , N - 1
        while left <= right:
            mid =  left + (right-left)//2
            if nums[mid] ==  target:
                return True

            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid+1
                elif  nums[mid] > target:
                    right = mid-1
            else:
                if nums[mid] >= nums[right]:
                    if nums[left] >= target and  nums[mid] > target:
                        left = mid + 1
                    else:
                        right =  mid - 1
                else:
                    if nums[right] <= target and  nums[mid] < target:
                        right = mid - 1
                    else:
                        left =  mid + 1
        
        return False

s = Solution()
search = s.search
print(search([4,5,6,7,0,1,2,3],7))
print(search([4,5,6,7,8,1,2,3],2))
print(search([1,3],0))


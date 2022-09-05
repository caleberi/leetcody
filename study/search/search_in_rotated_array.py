
# from typing import List

# def find_boundary(l:List[int],target):
#     if len(l)==1:
#         return (0,0)
#     i = 0
#     j = len(l)-1
#     while i<=j:
#         mid = (i+(j-i))//2
#         if l[mid] > l[0]:
#             return (mid+1,j) if target < l[mid] else (i,mid)
#         elif l[mid] < target:
#             i = mid+1
#         elif l[mid] > target:
#             j = mid-1
#     return (-1,-1)

# def binary_search(i,j,l,target):
#     mid = 0
#     while i<=j:
#         mid = (i + j) // 2
#         if l[mid] < target:
#             i = mid+1
#         elif l[mid] > target:
#             j = mid-1
#         else:
#             return mid
#     return -1


# def search(nums: List[int], target: int) -> int:
#     i,j=find_boundary(nums,target)
#     if i==-1 and j==-1:
#         return -1
#     return binary_search(i,j,nums,target)

# print(search([4,5,6,7,0,1,2,3],7))
# print(search([4,5,6,7,8,1,2,3],2))
# print(search([1,3],0))

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = left + (right- left) // 2
            if nums[mid]==target:
                return  mid
            # normal sorted array case
            if nums[left]<nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1

            else: 
                if nums[mid] >= nums[right]:
                    if nums[left] <= target < nums[mid]:
                        right = mid-1
                    else:
                        left = mid+1
                else:
                    if nums[right] >= target > nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
        return -1

s = Solution()
search = s.search
print(search([4,5,6,7,0,1,2,3],7))
print(search([4,5,6,7,8,1,2,3],2))
print(search([1,3],0))
         
                        

            
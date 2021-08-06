class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #         i=0
        #         while i< len(nums):
        #             if nums[i]==val:
        #                 j=len(nums)-i-1
        #                 while j>=i:
        #                     if nums[i]==val and nums[j]!=val:
        #                         self.swap(i,j,nums)
        #                         break;
        #                     elif nums[i]==val and nums[j]==val:
        #                         j-=1
        #                 i+=1
        #             else:
        #                 i+=1

        #         return len(nums)-nums.count(val)
        temp = None
        for i in range(len(nums)-1):
            current = nums[i]  # 0
            temp = len(nums)-1 if temp is None else temp  # 2
            if i == temp:
                break
            if current == val and nums[temp] != val:
                self.swap(i, temp, nums)
                temp -= 1
            elif current == val and nums[temp] == val:
                while temp > current and nums[temp] == val:
                    temp -= 1
                if nums[temp] != val:
                    self.swap(i, temp, nums)
        return len(nums)-nums.count(val)

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

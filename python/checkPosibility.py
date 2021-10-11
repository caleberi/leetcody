class Solution(object):
    def checkPossibility(self, nums):
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def isNonDecreasing(nums):
            for idx in range(1, len(nums)):
                if nums[idx] < nums[idx-1]:
                    return False
            return True

        def checkPossibilityHelper(arr, start, end):
            if len(arr) == 0:
                return []
            if isNonDecreasing(arr):
                return True

            for idx, num in enumerate(nums):
                subarr = nums[idx+1:]+nums[:idx-1]
                checkPossibilityHelper(subarr,)

        ret = checkPossibilityHelper(num, 0, len(nums))

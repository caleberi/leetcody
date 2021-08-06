class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pointer = 0
        hashMap = {}
        while pointer < len(nums):
            currentNumber = nums[pointer]
            if currentNumber in hashMap and pointer - hashMap[currentNumber] <= k:
                return True
            else:
                hashMap[currentNumber] = pointer
            pointer += 1
        return False

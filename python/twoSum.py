class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx in range(len(nums)):
            currentNum = nums[idx]
            difference = target-currentNum
            if difference not in hashMap and currentNum not in hashMap:
                hashMap[difference] = idx
            else:
                return [hashMap[currentNum], idx]

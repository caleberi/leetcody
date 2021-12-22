from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def obeys_condition(i,j,arr):
            return arr[i] % arr[j] == 0 or arr[j]
        pass
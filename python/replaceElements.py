class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = arr[-1]
        arr[-1] = -1
        idx = len(arr)-2
        while idx >= 0:
            holder = arr[idx]
            greatestElem = max(prev, arr[idx+1])
            arr[idx] = greatestElem
            prev = holder
            idx -= 1

        return arr

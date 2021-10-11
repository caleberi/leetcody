class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        highestPeakIdx = self.getHighestPeak(arr)
        print(highestPeakIdx)
        return self.desendToLeft(arr, 0, highestPeakIdx) and self.desendToRight(arr, len(arr)-1, highestPeakIdx)

    def desendToLeft(self, arr, end, pos):
        if end == pos:
            return False
        while pos > end:
            if arr[pos] <= arr[pos-1]:
                return False
            pos -= 1
        return True

    def desendToRight(self, arr, end, pos):
        if end == pos:
            return False
        while pos < end:
            if arr[pos] <= arr[pos+1]:
                return False
            pos += 1
        return True

    def getHighestPeak(self, arr):
        m = float("-inf")
        midx = 0
        for idx in range(len(arr)):
            if arr[idx] > m:
                m = arr[idx]
                midx = idx
        return midx

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pd = 0
        length = len(arr)-1
        for left in range(length+1):
            if left > length-pd:
                break
            if arr[left] == 0:
                if left == length-pd:
                    arr[length] = 0
                    length -= 1
                    break
                pd += 1

        last = length-pd
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+pd] = 0
                pd -= 1
                arr[i+pd] = 0
            else:
                arr[i+pd] = arr[i]

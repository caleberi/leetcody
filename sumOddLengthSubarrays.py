class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        total = 0
        s = set()
        for l in range(1, len(arr)+1):  # 1,2,3,4,5
            if l % 2 == 1:
                for i in range(len(arr)):
                    a = arr[i:i+l]
                    d = str(i) + ": " + '+'.join([str(v) for v in a])
                    if len(a) % 2 == 1 and d not in s:
                        s.add(d)
                        total += sum(a)
        return total

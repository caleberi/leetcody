class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {}
        b = {}
        for num in nums1:
            if num not in a:
                a[num] = [num]
            else:
                a[num].append(num)

        for num in nums2:
            if num not in b:
                b[num] = [num]
            else:
                b[num].append(num)
        ret = []
        for key, val in a.items():
            if key in b:
                l1 = len(a[key])
                l2 = len(b[key])
                temp = []
                if l1 > l2:
                    temp = b[key]
                elif l2 > l1:
                    temp = a[key]
                else:
                    temp = b[key] or a[key]
                ret.extend(temp)
        return ret

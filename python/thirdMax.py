class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sn = sorted(nums, reverse=True)
        mxc = 1
        mx = sn[0]
        tmn = sn[0]
        for i in range(len(nums)):
            if mxc == 3:
                return tmn
            if sn[i] < tmn:
                tmn = sn[i]
                mxc += 1
        return tmn if mxc == 3 else mx

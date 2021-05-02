class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
#         notToBeMoved=0
#         haveToBeMoved=0
#         maxHeightSoFar=heights[0]
#         for i in range(1,len(heights)):
#             currentHeight=heights[i]
#             if currentHeight> maxHeightSoFar:
#                 maxHeightSoFar=max(maxHeightSoFar,currentHeight)
#             if currentHeight < maxHeightSoFar:
#                 haveToBeMoved+=1
#             else:
#                 notToBeMoved+=1

#         return count
        count = 0
        sortedHeight = list(sorted(heights))
        for i in range(len(heights)):
            if heights[i] != sortedHeight[i]:
                count += 1
        return count

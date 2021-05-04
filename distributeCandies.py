class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candyType.sort()
        maxDailyCount = len(candyType)//2
        count = 1
        currentCandy = candyType[0]
        for idx in range(len(candyType)):
            currentCandyAtIdx = candyType[idx]
            if currentCandyAtIdx != currentCandy and count < maxDailyCount:
                count += 1
                currentCandy = currentCandyAtIdx
        return count

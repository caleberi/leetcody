class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsMap = createMap(jewels)
        stoneMap = createMap(stones)
        count = 0
        for key, _ in jewelsMap.items():
            if key in stoneMap:
                count += stoneMap[key]
        return count


def createMap(string):
    frequency = {}
    for ch in string:
        if ch not in frequency:
            frequency[ch] = 1
        else:
            frequency[ch] += 1
    return frequency

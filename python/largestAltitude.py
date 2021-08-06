class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        if len(gain) == 0:
            return 0
        altitudes = [0]
        max_ = altitudes[0]
        for altitude in gain:
            previousAltitude = altitude + altitudes[-1]
            altitudes.append(previousAltitude)
            max_ = max(max_, previousAltitude)
        return max_

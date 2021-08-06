class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        locations = []
        for i in range(len(S)):
            ch = S[i]
            if ch == C:
                locations.append(i)
        print(locations)
        minDistances = [float("inf") for _ in range(len(S))]
        for location in locations:
            for idx in range(len(S)):
                dist = abs(location-idx)
                if minDistances[idx] > dist:
                    minDistances[idx] = dist
        return minDistances

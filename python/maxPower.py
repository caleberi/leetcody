
from typing import Counter


def maxPower(s):
    s += ' '
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    h = {}
    start = 0
    end = 0
    while start < len(s) and end < len(s):
        if s[end] == s[start]:
            end += 1
        elif s[end] != s[start]:
            if s[end-1] in h:
                if end-start > h[s[end-1]]:
                    h[s[end-1]] = end-start
                    start = end
                else:
                    start = end
            else:
                h[s[end-1]] = end-start
                start = end
    return max(list(h.values()))


print(maxPower("ccdddertyyyyyyyyyyyyisa"))
print(maxPower("leetcode"))
print(maxPower("abbcccddddeeeeedcba"))
print(maxPower("triplepillooooow"))

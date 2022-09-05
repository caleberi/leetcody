from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        s = zip(*strs)
        print(list(s))
        for i in s:
            if len(set(i)) ==1 :
                prefix += i[0]
            else:
                break
        return prefix

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
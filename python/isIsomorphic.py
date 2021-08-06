class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapA = {}
        hashMapB = {}
        for idx in range(len(s)):
            if s[idx] not in hashMapA and t[idx] not in hashMapB:
                hashMapA[s[idx]] = t[idx]
                hashMapB[t[idx]] = s[idx]
            else:
                if (s[idx] in hashMapA and hashMapA[s[idx]] and hashMapA[s[idx]] != t[idx]) or (t[idx] in hashMapB and hashMapB[t[idx]] and hashMapB[t[idx]] != s[idx]):
                    return False
        return True

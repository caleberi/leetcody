class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedCharacterSet = set(list(allowed))
        count = 0
        for word in words:
            flag = 0
            for ch in word:
                if ch not in allowedCharacterSet:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        return count

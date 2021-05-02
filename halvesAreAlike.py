class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return countVowel(s)


def countVowel(s: str):
    i = 0
    j = len(s)-1
    a = 0
    b = 0
    while i < j:
        if s[i] in 'aeiouAEIOU':
            a += 1
        if s[j] in 'aeiouAEIOU':
            b += 1
        i += 1
        j -= 1
    return a == b

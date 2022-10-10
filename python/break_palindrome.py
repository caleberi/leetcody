def isPalindrome(s:str) -> bool:
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False 
        i += 1
        j -= 1
    return True
    
# FAILED TIME LIMIT EXCEEDED  
# 22 / 30 test cases passed.
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        min_char,max_char= 97, 122
        temp_split = list(palindrome)
        temp_slit_cpy = temp_split[::]
        not_palindrome = {}
        smallest_non_palinromic = None
        for idx in range(len(palindrome)):
            i = ord(palindrome[idx])
            l = i - 1
            r = i + 1
            while l >= min_char or r <= max_char:
                if l >= min_char:
                    temp_slit_cpy[idx] = chr(l)
                    s = ''.join(temp_slit_cpy)
                    if s not in not_palindrome:
                        if not isPalindrome(s):
                            if smallest_non_palinromic is None:
                                smallest_non_palinromic = s
                            else:
                                smallest_non_palinromic = s if s < smallest_non_palinromic else smallest_non_palinromic
                        not_palindrome[s]=True
                    l -= 1
                if r <= max_char:
                    temp_slit_cpy[idx] = chr(r)
                    s = ''.join(temp_slit_cpy)
                    if s not in not_palindrome:
                        if not isPalindrome(s):
                            if smallest_non_palinromic is None:
                                smallest_non_palinromic = s
                            else:
                                smallest_non_palinromic = s if s < smallest_non_palinromic else smallest_non_palinromic
                        not_palindrome[s]=True
                    r += 1
            temp_slit_cpy = temp_split[::]
                
        return smallest_non_palinromic if smallest_non_palinromic else ""


    def breakPalindrome(self, palindrome: str) -> str:
        n =  len(palindrome)
        if n==1:
            return ""
        temp = list(palindrome)
        for idx in range(n//2):
            if palindrome[idx] != "a":
                temp[idx] = "a"
                return ''.join(temp)
        temp[n-1] = "b"
        return ''.join(temp)
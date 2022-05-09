class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not len(s):
            return True
        s =  s.lower()
        s = "".join(filter(str.isalnum, s))
        return self.validPalindrome(s,0,len(s)-1)
        
    def validPalindrome(self,s:str,i:int,j:int) -> bool:
        while i <= j:
            if s[i] != s[j]:
                return False 
            i += 1
            j -= 1
        return True



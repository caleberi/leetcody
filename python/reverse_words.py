class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        r = []
        stk = []
        for i in range(len(s)):
            if s[i] != ' ':
                stk.append(s[i])
            else:
                if len(stk) and stk[-1] != ' ':
                    r.append(''.join(stk))
                    stk = []
                    
        if len(stk) and stk[-1] != ' ':
            r.append(''.join(stk))
            stk = [] 
        
        return ' '.join(r[::-1])
            

# 334 / 334 test cases passed.
# Status: Accepted
# Runtime: 41 ms
# Memory Usage: 13.9 MB
class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1,len(s)):
            curr = s[i]
            
            f = stack and stack[-1] == curr.lower() and curr.isupper()
            b = stack and stack[-1] == curr.upper() and curr.islower()
            
            if f or b:
                stack.pop()
            else:
                stack.append(curr)
        
        return "".join(stack)

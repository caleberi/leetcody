# 20 / 20 test cases passed.
# Status: Accepted
# Runtime: 153 ms
# Memory Usage: 18.7 MB
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [["$",0]] 
        for i in range(len(s)):
            ch = s[i]
            
            if stk[-1][0] == ch:
                stk[-1][1] += 1
            else:
                stk.append([ch,1])
            if stk[-1][1] == k:
                stk.pop()
        return "".join([ s[0]*s[1] for s in stk[1:]])

if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicates("deeedbbcccbdaa",3) == "aa"
    assert s.removeDuplicates("abcd",2) == "abcd"
    assert s.removeDuplicates("pbbcggttciiippooaais",2) == "ps"
    assert s.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4) == "ybth"
    
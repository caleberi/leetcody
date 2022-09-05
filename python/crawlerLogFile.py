from typing import List


# 99 / 99 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Memory Usage: 14.2 MB

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for i in range(0,len(logs)):
            if logs[i] ==  "../":
                if len(stk):
                    stk.pop()
            elif logs[i] == "./":
                continue
            else:
                stk.append(logs[i])
        if len(stk) == 1 and stk[0] == "./":
            return 0
        return len(stk)

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
    print(s.minOperations(["d1/","../","../","../"]))
    print(s.minOperations(["1/"]))
    print(s.minOperations(["./","../","./"]))
    print(s.minOperations(["./","ho3/","tl8/"]))
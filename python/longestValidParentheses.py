class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) == 0:
            return 0
        stack = [-1]
        result = 0
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    length = idx-stack[-1]
                    result = max(result, length)
        return result


def longestParentheses(string):
    if len(string) == 0:
        return 0
    stk = []
    longestLength = 0
    for i, ch in enumerate(string):
        if ch == '(':
            stk.append(i)
        elif ch == ')':
            if stk:
                open_i = stk.pop()
                length = i-open_i + 1
                if length > longestLength:
                    longestLength = length
    return longestLength

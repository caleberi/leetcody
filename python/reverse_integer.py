"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
"""


class Solution:
    def reverse(self, x: int) -> int:
        x_st = list(str(x))
        if x_st[0] in ["+", "-"]:
            sign = x_st[0]
            x_st = x_st[1::]
            x_st.reverse()
            x_st.insert(0, sign)
            rev = "".join(x_st)
            return int(rev) if (-2**31) < int(rev) < (2**31 - 1) else 0
        else:
            x_st.reverse()
            rev = "".join(x_st)
            return int(rev) if (-2**31) < int(rev) < (2**31 - 1) else 0

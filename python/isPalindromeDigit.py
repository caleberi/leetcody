class Solution(object):
    def isPalindrome(self, x):
        string = str(x)
        number = x
        digit = 0
        while number > 0:
            digit += 1
            number = number // 10
        rnumber = 0
        i = len(string)-1
        while digit > 0:
            rnumber += int(string[i]) * (10**(digit-1))
            digit -= 1
            i -= 1
        return rnumber == x

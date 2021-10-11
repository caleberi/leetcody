import math as mth


class Solution(object):
    def superpalindromesInRange(self, left, right):
        def palindrome(string):
            return string[::-1]==string,int(string)
        
        for number in range(int(left), int(right)+1):
            isPalindromeNumber, palindromeNumber = palindrome(str(number))
            if isPalindromeNumber:
                squareRoot = mth.sqrt(palindromeNumber)
                isPerfectSquareRoot = (int(squareRoot)*int(squareRoot))==palindromeNumber
                if isPerfectSquareRoot:
                    isPalindromeNumberSqrt, palindromeNumberSqrt = palindrome(str(squareRoot))
                    if isPalindromeNumberSqrt:
                        count+=1
        return count

# 185 / 185 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 13.9 MB

from typing import List



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def get_clean_local_name(local_name:str):
            split_by_plus = local_name.split('+') #0(N)
            cleaned_local_name = ""
            for i in range(len(split_by_plus[0])): #0(N)
                if split_by_plus[0][i] == ".":
                    continue
                # I thought a string builder will increase efficience but I was quite wrong
                # 0(N) is apparently the worst time complexity
                cleaned_local_name += split_by_plus[0][i]
            return cleaned_local_name

        def clean_email(email:str):
            split_by_email_symbol = email.split('@') #0(N)
            clean_local_name = get_clean_local_name(split_by_email_symbol[0]) 
            return clean_local_name+"@"+split_by_email_symbol[1]

        l = []
        for email in emails:
            l.append(clean_email(email))
        answer = set(l)
        return len(answer)



# 185 / 185 test cases passed.
# Status: Accepted
# Runtime: 158 ms
# Memory Usage: 14.1 MB
class StringBuilder(object):
    def __init__(self) -> None:
        self.store = [""]

    def __iadd__(self, value):
        """appends a character to the sequence"""
        self.store.append(value)
        return self
    
    def clear(self):
        self.store = [""]

    def __str__(self) -> str:
        """string representation from the built sequence"""
        return "".join(self.store)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def get_clean_local_name(local_name:str):
            split_by_plus = local_name.split('+') #0(N)
            cleaned_local_name = StringBuilder()
            for i in range(len(split_by_plus[0])): #0(N)
                if split_by_plus[0][i] == ".":
                    continue
                cleaned_local_name += split_by_plus[0][i] #0(N) but can be improved using string builder [WRONG]
            return str(cleaned_local_name)

        def clean_email(email:str):
            split_by_email_symbol = email.split('@') #0(N)
            clean_local_name = get_clean_local_name(split_by_email_symbol[0]) 
            return clean_local_name+"@"+split_by_email_symbol[1]
        l = []
        for email in emails:
            l.append(clean_email(email))
        answer = set(l)
        return len(answer)

    


if __name__ == "__main__":
    s = Solution()
    result = s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    assert result == len(["testemail@leetcode.com","testemail@lee.tcode.com"])
    result = s.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
    assert result == len(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])

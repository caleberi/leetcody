class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(" ")
        print(s_split)
        for i in range(len(s_split)):
            rev = s_split[i][::-1]
            s_split[i]= rev
        return " ".join(s_split)
        
class Solution:
    def letterCasePermutation(self, s):
            def letterCasePermutationHelper(s,i,seen):
                if i==len(s):
                    return
                for j in range(i,len(s)):
                    ch = s[j]
                    if ch.isalpha():
                        if ch.islower():
                            s[j] = ch.upper()
                            new_string = "".join(s)
                            if new_string not in seen:
                                seen.add(new_string)
                            letterCasePermutationHelper(s,j+1,seen)
                            s[j] = ch.lower()
                        if ch.isupper():
                            s[j] = ch.lower()
                            new_string = "".join(s)
                            if new_string not in seen:
                                seen.add(new_string)
                            letterCasePermutationHelper(s,j+1,seen)
                            s[j] = ch.upper()
                
            seen = {s}
            letterCasePermutationHelper(list(s),0,seen)
            return list(seen)
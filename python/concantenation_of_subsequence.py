from typing import List


class Solution:
    def __init__(self) -> None:
        self.max_length = 0

    def maxLength(self, arr: List[str]) -> int:
        
        # formed by concatenation of subsequence 
        def check_for_uniqueness(s):
            return len(set(list(s)))==len(s)
        
        def dfs(arr, i, s):
            if check_for_uniqueness(s) :
                self.max_length = max(self.max_length,len(s))

            if i == len(arr) or not check_for_uniqueness(s):
                return 
                
            for i in range(i,len(arr)):
                dfs(arr, i+1, s + arr[i])

        if arr is None or len(arr) == 0:
            return 
            
        dfs(arr,0,'')

        return self.max_length


if __name__ == "__main__":
    s = Solution()
    print(s.maxLength(["un","iq","ue"]))
    print(s.maxLength(["cha","r","act","ers"]))
    print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    print(s.maxLength(["aa","bb"]))
    print(s.maxLength(["ab","ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"]))
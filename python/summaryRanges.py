from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s = []
        i = 0 
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                i+=1
            if start != nums[i]:
                s.append(f"{start}->{nums[i]}")
            else:
                s.append(f"{start}")
            i+=1
        return s
    
    #  Brute force failed 24/29 
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not len(nums):
            return []
        i = nums[0] # -2147483648
        j = 0
        result = []
        s =  [] 
        t = 0
        while j < len(nums):
            curr = nums[j]
            if t == 3:
                break
            if curr == i:
                s.append(i)
            elif curr != i:
                if len(s)>1:
                    result.append(str(s[0])+'->'+str(s[len(s)-1]))
                    s.clear()
                if len(s)==1:
                    result.append(str(s[0]))
                    s.clear()
                i += 1
                continue
            i+=1
            j += 1
        if len(s)>1:
            result.append(str(s[0])+'->'+str(s[len(s)-1]))
            s.clear()
        if len(s)==1:
            result.append(str(s[0]))
            s.clear()
            
        return result
            
            
        
if __name__ == "__main__":
    c = Solution()
    c.summaryRanges([-2147483648,-2147483647,2147483647])


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 882 ms
# Memory Usage: 19.7 MB

from typing import List

def sortStack(stack):
    if len(stack)==0:
        return stack
    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack,top)
    return stack

def insertInSortedOrder(stack,value):
    if len(stack) == 0 or stack[-1][1] <= value[1]:
        stack.append(value)
        return
    top=stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 1 
            else:
                table[num]+=1 
        r = sortStack([[k,v] for k,v in table.items()])
        ans = []
        i = 0;
        while i < k:
            ans.append(r.pop()[0])
            i += 1
        return ans




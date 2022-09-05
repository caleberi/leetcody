

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Idea :  to have the smallest digit after k removal
        # we have to start from the front or back and then compare the digit 
        # for the smallest 

        def fx(num:str, k:int, d:int):
            
            if k > len(num):
                return "0"

            if len(num) == 1 and k == 1:
                return "0"

            stk = [] 
            i = 0 if d > 0 else len(num)-1
            while (i >= 0 and i < len(num)):
                
                # if k > 0:
                #     c = int(num[i]) # pick the current digit
                #     if len(stk) and int(stk[-1]) < c:
                #         k -= 1
                #     elif len(stk) and int(stk[-1]) > c : # 
                #         stk.pop()
                #         stk.append(num[i])
                #         k -= 1
                #     elif not len(stk):
                #         stk.append(num[i])
                # elif k < 0 and (i >= 0 or i < len(num)):
                #     stk.append(num[i])
                #     i = i+1 if d > 0 else i-1
                #     continue
                # i = i+1 if d > 0 else i-1
                
            print(f"**: stk = {stk}  num[i:] = {num[i:]}")
            return ''.join(stk) + num[i:]

        if len(num) == 1 and k == 1:
            return "0"
        x = int(fx(num,k,1)) 
        y = int(fx(num,k,-1)) 
        return str(x) if x < y else str(y)  


if __name__ == "__main__":
    s = Solution()
    print(s.removeKdigits("1432219",3))
    print(s.removeKdigits("10",2))
    print(s.removeKdigits("112",1))
    print(s.removeKdigits("5337",2))
    print(s.removeKdigits("111111",3))
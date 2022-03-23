

# class Solution:
#     def convert(self, s, numRows):
#         if numRows == 1:
#             return s

#         a = [" " for i in range(numRows)] # ["","","","","","",""]
#         c =  numRows
#         inc = False
#         for ch in s:
#             a[numRows-c]+=ch
#             if not inc:
#                 c -= 1
#                 if c==1:
#                     inc = True
#             else:
#                 c += 1
#                 if c==numRows:
#                     inc = False
#         return "".join(a)

class Solution:
    def convert(self, s, numRows):
        if numRows==1 or len(s)==1 or len(s)==0:
            return s
        a = {}
        down = True
        i = 0
        for j in range(len(s)):
            if i==numRows-1 and down:
                down=False
            if i==0 and not down:
                down=True
            if i not in a:
                a[i]=s[j]
            else:
                a[i]+=s[j]
            
            if down:
                i+=1
            else:
                i-=1
        s = ""
        i = 0
        for i in range(numRows):
            s+=a[i]
        return s

    
s = Solution()
print(s.convert("PAYPALISHIRING",3))
"""

Given an encoded string, s, return its decoded representation. 
The string s will be encoded as follows N[letters], meaning that the letters should
be repeated N times in the decoded representation.
Note: You may assume s always encoded correctly 
(i.e. correct formatting of brackets, only positive values outside the brackets,
 and always lowercase alphabetical characters inside the brackets).

Ex: Given the following string s ...

s = "3[a]2[b]1[c]", return "aaabbc" ("a" is repeated 3 times, "b" is repeated 2 times, and "c" is repeated 1 time).
Thanks,
The Daily Byte

"""



class StringBuilder(object):
    def __init__(self, val):
        self.store = [val]

    def __iadd__(self, value):
        self.store.append(value)
        return self

    def clear(self):
        self.store.clear()

    def __str__(self):
        return "".join(self.store)

# def clean_stack(stk,last_open,i):
#     while i > last_open[-1]+1:
#         stk.pop()
#         i-=1


# def expand(string,stk,last_open,i):
#     string_before_open = StringBuilder("") 
#     j = last_open[-1]+1
#     while j < i:
#         if(string[j]=="[" or string[j].isdigit() or string[j]=="]"):
#             break
#         string_before_open+=string[j]
#         j+=1
   
#     clean_stack(stk,last_open,i)
#     decoded_string = StringBuilder("")
#     while len(stk) and  stk[-1]:
#         decoded_string+=str(string_before_open)
#         stk[-1]-=1
#     string[last_open[-1]+1:i-1] = list(str(decode_characters))
#     # last_open.pop()

#     if len(stk) and isinstance(stk[-1],int): 
#         stk.pop()
#         stk.append(str(decoded_string))
#         decoded_string.clear()
#         print(last_open)
#         print(string_before_open)
#         print(stk)
#     # 
#     #     if stk[-1]=="[":
#     #         temp = stk[-1]
#     #         stk.pop()
#     #         stk.append(temp)
      
def expand(string,stk,last_open,i):
    string_before_open = StringBuilder("") 
    j = last_open[-1]+1
    while j < i:
        string_before_open+=string[j]
        j+=1
    # clean_stack(stk,last_open,i)
#     decoded_string = StringBuilder("")
#     while len(stk) and  stk[-1]:
#         decoded_string+=str(string_before_open)
#         stk[-1]-=1

# def decode_characters(string):
#     if len(string) == 0 :
#         return ""
    
#     stk = []
#     last_open = []
#     curr_num = StringBuilder("")
#     string = list(string)
#     for i in range(len(string)):
#         char = string[i]
#         if char == "]":
#             expand(string,stk,last_open,i)
#         elif char.isdigit():
#             curr_num+=char
#         elif char == "[":
#             last_open.append(i)
#             stk.append(int(curr_num.__str__()))
#             curr_num.clear()
#         else:
#             stk.append(char)
#     return "".join(stk)



if __name__ == "__main__":
    print(decode_characters("3[a]4[b]5[c4[u]]"))


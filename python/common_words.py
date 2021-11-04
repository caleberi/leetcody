"https://binarysearch.com/problems/Common-Words"
class Solution:
    def solve(self, s0, s1):
        if s0=="" and s1=="":
            return 0
        s0 = s0.lower()
        s1 = s1.lower()
        h_1 = {}
        h_2 = {}
        count =0
        sl_0 = s0.split(" ")
        sl_1 = s1.split(" ")
        for s in sl_0:
            if s not in h_1:
                h_1[s] = 1
        
        for s in sl_1:
            if s not in h_2:
                h_2[s] = 1

        table_to_use = h_2 if max(len(h_1),len(h_2)) == len(h_2) else h_1
        table_to_check = h_2 if table_to_use == h_1 else  h_1
        count = 0
        for k in table_to_use.keys():
            if k  in table_to_check:
                count+=1
        return count 

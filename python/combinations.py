from itertools import combinations
class Solution:
    def combine(self, n,k):
        # def permutate(m,i,d,result=[]):
        #     if i==d:
        #         return result.append(m[d-i:i])
        #     if i==len(m)-1:
        #         return result.append(m[:])
        #     for j in range(i,len(m)):
        #         m[0],m[j] = m[j],m[0]
        #         permutate(m,i+1,d,result)
        #         m[0],m[j] = m[j],m[0]
            
        # result = []
        # l = [i for i in range(1,n+1)]
        # permutate(l,0,k,result)
        # s = set()
        # for num in result:
        #     s.add(tuple(num))
        # l = map(lambda x : list(x),s)
        # return l
        c = combinations([i for i in range(1,n+1)],k)
        l=[]
        for x in c:
            l.append(list(x))
        return l

s =Solution()
print(s.combine(4,2))



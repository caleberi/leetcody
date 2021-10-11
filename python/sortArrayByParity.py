class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        if len(arr) == 0 or len(arr) == 1:
            return arr
        i = 0
        j = len(arr)-1
#         while j>=i:
#             if isOdd(arr[i]) and not isOdd(arr[j]):
#                 arr[i],arr[j]=arr[j],arr[i]
#                 i+=1
#                 j-=1
#             elif isOdd(arr[i]) and isOdd(arr[j]):
#                 j-=1
#             elif not isOdd(arr[i]) and not isOdd(arr[i]):
#                 i+=1
#             elif not isOdd(arr[i]) and isOdd(arr[j]):
#                 i+=1
#             elif not isOdd(arr[i]) and not isOdd(arr[j]):
#                 i+=1
#                 j-=1

        while j >= i:
            iParity = arr[i] % 2
            jParity = arr[j] % 2
            if jParity < iParity:
                arr[i], arr[j] = arr[j], arr[i]
            if iParity == 0:
                i += 1
            if jParity == 1:
                j -= 1

        return arr


def isOdd(n):
    if n == 0:
        return False
    return n % 2 == 1

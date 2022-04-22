
# 41 / 41 test cases passed.
# Status: Accepted
# Runtime: 215 ms
# Memory Usage: 18 MB

from ast import Str
from typing import List

 
class StringBuilder(object):
    def __init__(self) -> None:
        self.store = [""]

    def __iadd__(self, value):
        """appends a character to the sequence"""
        self.store.append(value)
        return self
    
    def clear(self):
        self.store = [""]

    def __str__(self) -> str:
        """string representation from the built sequence"""
        return "".join(self.store)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def binary_search(word:str,first:int,end:int,result:List[str]):
            if first > end:
                return
            mid = (first + (end-first)//2) 
            if products[mid].startswith(word):
                result.append(products[mid])
                binary_search(word,first,mid-1,result)
                binary_search(word,mid+1,end,result)
            elif products[mid][:len(word)+1] > word:
                return  binary_search(word,first,mid-1,result)
            elif   products[mid][:len(word)+1] < word:
                return binary_search(word,mid+1,end,result)

        products.sort() # sorted lexicographically 
        ret = []
        word_fragement = StringBuilder()
        for idx in range(len(searchWord)):
            result = []
            word_fragement+=searchWord[idx] 
            binary_search(str(word_fragement),0,len(products)-1,result)
            result.sort()
            ret.append(result[:3])

        return ret
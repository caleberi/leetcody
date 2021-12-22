class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = "*"

    def add(self, word):
        node = self
        wordfar = ""
        for ch in word:
            wordfar += ch
            if ch not in node.children:
                node.children[ch] = TrieNode()
                node.children[ch].word = wordfar
            node = node.children[ch]
        node.word = wordfar

    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return "*"
            node = node.children[ch]
        return node.word
    
def is_valid(word,puzzle):
    
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ret = []
        for i in range(len(puzzles)):
            count=0
            for j  in range(len(words)):
                if is_valid(words[j],puzzles[i]):
                    count+=1
            ret.append(count)
    
                    
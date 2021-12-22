class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.symbol = "*"
        self.word = '$'

    def search(self,word):
        root =  self
        for ch in word:
            if ch not in root.children:
                if word != root.word:
                    return False
        return root.word == word

        
    def insert(self,word):
        root =  self
        built_word = ''
        for ch in word:
            if ch not in root.children:
                root.children[ch]= TrieNode()
                built_word+=ch
                root.word = built_word
            else:
                root = root.children[ch]
        if root.symbol == "*":
            root.symbol = word
        root.word = word
            
        
class StreamChecker:

    def __init__(self, words):
        self.trie = self.build_trie(words)

    def build_trie(self,words):
        trie = TrieNode()
        for word in words:
            for i in range(len(word)):
                trie.insert(word[i:])
        return trie

    def query(self, letter):
        pass
        

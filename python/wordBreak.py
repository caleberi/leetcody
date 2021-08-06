# Given a string s and a dictionary of strings wordDict, return true
# if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

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


def wordBreak(string, dictionary):
    if string == "":
        return False
    if len(dictionary) == 0:
        return True
    trie = TrieNode()
    for i in range(len(string)):
        word = string[i:]
        trie.add(word)

    for word in dictionary:
        if trie.search(word) == "*":
            return False
    return True


if __name__ == "__main__":
    print(wordBreak("leetcode", ["leet", "code"]))
    print(wordBreak("applepenapple", ["apple", "pen"]))
    print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(wordBreak("mummy", ["mum", "my", "mummy"]))

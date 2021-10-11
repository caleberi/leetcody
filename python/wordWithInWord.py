"""
Given an array of words, return all strings in words that are a substring of another word.
Note: The order in which you return the substrings does not matter.

Ex: Given the following words…

words = ["abc", "a", "b"], return ["a", "b"].
Ex: Given the following words…

words = ["ab", "ba", "c"], return [].
"""

from typing import Set


class TrieNode:
    def __init__(self):
        self.children = {}
        self.symbol = "*"

    def insert(self, word):
        node = self
        wordSoFar = ""
        for i in range(len(word)):
            letter = word[i]
            wordSoFar += letter
            if letter is not node.children:
                node.children[letter] = TrieNode()
                node.children[letter].symbol = wordSoFar
            node = node.children[letter]
        node.children[node.symbol] = wordSoFar

    def search(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True


def wordWithinWord(words):
    trie = TrieNode()
    result = set()  # type: Set[str]
    for i in range(len(words)):
        word = words[i]
        for j in range(len(word)):
            # create a trie for the each current substring in the current word
            trie.insert(word[j:])
        for k in range(i+1, len(words)):
            # search for all words present in the  current trie just formed by
            # for current idx + 1 forward
            searchKey = words[k]
            if trie.search(searchKey):
                result.add(searchKey)
    return list(result)


"""
     *
     |  [a]  [ab]
     -> a -> b ->*
     |  [b]  [ba]
     -> b -> a ->*
     |  [c]
     -> c ->*
"""

if __name__ == "__main__":
    words = ["cat", "cats", "catsdogcats", "catxdogcatsrat", "dog",
             "dogcatsdog", "hippopotamuses", "rat", "ratcat", "life", "food", "money", "hippo"]
    # words = ["ab", "ba", "c"]
    # words = ["abc", "a", "b"]
    print(wordWithinWord(words))

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        return palindromePairs(words)


class Node:
    def __init__(self):
        self.children = {}
        self.indices = []
        self.index = -1


def insert(root, word, idx):
    current = root
    for (i, ch) in enumerate(word):
        if isPalindrome(word, i, len(word)-1):
            current.indices.append(idx)
        if ch not in current.children:
            current.children[ch] = Node()
        current = current.children[ch]
    current.indices.append(idx)
    current.index = idx


def search(root, word, idx, result):
    current = root
    for (i, ch) in enumerate(word):
        if current.index != -1 and isPalindrome(word, i, len(word)-1):
            result.append([idx, current.index])
        if ch not in current.children:
            return
        current = current.children[ch]
    for match in current.indices:
        if match != idx:
            result.append([idx, match])


def palindromePairs(words: list[str]) -> list[list[int]]:
    root = Node()
    for (idx, word) in enumerate(words):
        insert(root, word[::-1], idx)

    result = []
    for (idx, word) in enumerate(words):
        search(root, word, idx, result)
    return result


def isPalindrome(word, start, end) -> bool:
    i = start
    j = end
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

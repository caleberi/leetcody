import unittest


# class WordFilter(object):

#     def __init__(self, words):
#         self.words = words
#         self.trie = Trie()

#     def f(self, prefix, suffix):
#         """
#         :type prefix: str
#         :type suffix: str
#         :rtype: int
#         """
#         for idx, word in enumerate(self.words):
#             self.trie.insertForward(word, idx)
#             self.trie.insertBackward(word, idx)
#         prefixFound = self.trie.find(prefix)
#         suffixFound = self.trie.find(suffix)
#         if prefixFound != [] and suffixFound != []:
#             intersect = prefixFound & suffixFound
#             return max(intersect)
#         else:
#             return -1


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, info):
#         word, idx = info
#         root = self.root
#         wordSoFar = ""
#         for ch in word:
#             wordSoFar += ch
#             if ch not in root.children:
#                 root.children[ch] = TrieNode()
#                 root.children[ch].symbol = wordSoFar
#                 root.children[ch].idxs.append(idx)
#             else:
#                 root = root.children[ch]

#     def find(self, word):
#         root = self.root
#         ret = []
#         for ch in word:
#             if ch not in root.children:
#                 return []
#             else:
#                 root = root.children[ch]
#                 ret.extend(root.idxs)
#         print(ret)
#         return set(ret)

#     def insertForward(self, word, idx):
#         self.insert((word, idx))

#     def insertBackward(self, word, idx):
#         self.insert((word[::-1], idx))


# class TrieNode:
#     def __init__(self):
#         self.symbol = "*"
#         self.children = {}
#         self.idxs = []


# # Your WordFilter object will be instantiated and called as such:
# # obj = WordFilter(words)
# # param_1 = obj.f(prefix,suffix)

class WordFilter(object):
    def __init__(self, words):
        self.prefix_dict = {}
        self.suffix_dict = {}
        self.cache = {}
    # 0(N^2)time | 0(2N) space
        for wordidx, word in enumerate(words):
            idx = 0
            while idx <= len(word):
                prefix = word[:idx]
                suffix = word[len(word)-idx:]
                if prefix not in self.prefix_dict:
                    self.prefix_dict[prefix] = {wordidx}
                else:
                    self.prefix_dict[prefix].add(wordidx)
                if suffix not in self.suffix_dict:
                    self.suffix_dict[suffix] = {wordidx}
                else:
                    self.suffix_dict[suffix].add(wordidx)
                idx += 1

    def f(self, prefix, suffix):
        if (prefix, suffix) in self.cache:
            return self.cache[(prefix, suffix)]
        ans = -1
        prefixFound = self.prefix_dict.get(prefix)  # 0(1) lookup
        suffixFound = self.suffix_dict.get(suffix)
        if (prefixFound is not None) and (suffixFound is not None):
            lans = list(prefixFound & suffixFound)
            if len(lans) > 0:
                ans = max(lans)  # 0(max(N))
        self.cache[(prefix, suffix)] = ans
        return ans


class WordFilterTestCase(unittest.TestCase):
    def testCreateHash(self):
        w = WordFilter(["apple", "orange", "banana", "mango",
                        "return", "manufacture", "time"])
        # self.assertDictEqual(
        #     w.hash, {'a#': [0, 0], '#e': [0, 0, 1], 'ap#': [0, 0], '#le': [0, 0],
        #              'app#': [0, 0], '#ple': [0, 0], 'appl#': [0, 0],
        #              '#pple': [0, 0], 'apple#': [0, 0],
        #              '#apple': [0, 0], 'o#': [1, 1], 'or#': [1, 1],
        #              '#ge': [1, 1], 'ora#': [1, 1], '#nge': [1, 1],
        #              'oran#': [1, 1], '#ange': [1, 1],
        #              'orang#': [1, 1], '#range': [1, 1], 'orange#': [1, 1],
        #              '#orange': [1, 1], 'b#': [2, 2], '#a': [2, 2],
        #              'ba#': [2, 2], '#na': [2, 2], 'ban#': [2, 2],
        #              '#ana': [2, 2], 'bana#': [2, 2], '#nana': [2, 2],
        #              'banan#': [2, 2], '#anana': [2, 2],
        #              'banana#': [2, 2], '#banana': [2, 2], 'm#': [3, 3], '#o': [3, 3], 'ma#': [3, 3],
        #              '#go': [3, 3], 'man#': [3, 3], '#ngo': [3, 3], 'mang#': [3, 3], '#ango': [3, 3],
        #              'mango#': [3, 3], '#mango': [3, 3]}
        # )

        self.assertEqual(w.f("ti", "e"), 6)
        self.assertEqual(w.f("re", "n"), 4)
        self.assertEqual(w.f("manu", "ure"), 5)
        self.assertEqual(w.f("ba", "pple"), -1)
        self.assertEqual(w.f("app", "e"), 0)
        self.assertEqual(w.f("time", "e"), 6)


if __name__ == "__main__":
    unittest.main()

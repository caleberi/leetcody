class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word

    # Remove a word after you find an occurence!
    # Such an act can rescue a testcase like this:
    #
    # +---------+
    # | a a a a | Word list:
    # | a a a a |  - "aaa"
    # | a a a a |  - "aaaa"
    # | a a a a |  - "aaaaa"
    # +---------+
    #
    def remove_word(self, word):
        path = [self.root]
        for c in word:
            path.append(path[-1].children[c])
        path[-1].word = None
        for c in word[::-1]:
            if (path[-1].word is None) and len(path[-1].children) == 0:
                path.pop()
                del path[-1].children[c]
            else:
                break


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        result = []
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        curr_path = [trie.root]

        def valid(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:  # out of bound
                return False
            if visited[i][j]:  # cannot use a block twice
                return False
            if board[i][j] not in curr_path[-1].children:  # dead end
                return False
            return True

        moves = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        def backtrack(i, j):
            visited[i][j] = True
            c = board[i][j]
            curr_path.append(curr_path[-1].children[c])

            word = curr_path[-1].word
            if word is not None:  # found!
                result.append(word)
                trie.remove_word(word)

            for di, dj in moves:
                i0, j0 = i+di, j+dj
                if valid(i0, j0):
                    backtrack(i0, j0)

            curr_path.pop()
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                if valid(i, j):
                    backtrack(i, j)
        return result

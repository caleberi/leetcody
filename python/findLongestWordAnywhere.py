import collections
import copy
import itertools
from typing import Iterator, Iterable, List, Sequence, Set

Cell = collections.namedtuple("Cell", "x, y, letter")

# defaultdict-based implementation of a trie; for much more see URL:
# https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
# In an interview you don't have to code this, the problem clearly states that
# you have it available already.

_end = "_end_"


def _get_trie():
    return collections.defaultdict(_get_trie)


class Trie:
    """A defaultdict-based Trie implementation."""

    def __init__(self):
        self._trie = _get_trie()

    def add(self, word: str) -> None:
        curr = self._trie
        for letter in word:
            curr = curr[letter]
        curr.setdefault(_end)

    def is_word(self, word: str) -> bool:
        curr = self._trie
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return _end in curr

    def is_prefix(self, word: str) -> bool:
        curr = self._trie
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True


class Dictionary:
    """A dictionary of words."""

    def __init__(self, words: Iterable[str]) -> None:
        self._trie = Trie()
        for w in words:
            self._trie.add(w.strip())

    def is_word(self, word: str) -> bool:
        """Checks whether 's' is one of the words in the dictionary."""
        return self._trie.is_word(word)

    def is_prefix(self, word: str) -> bool:
        """Checks whether 's' the prefix of any of the words in the dictionary."""
        return self._trie.is_prefix(word)


class Grid:
    """A grid of letters."""

    def __init__(self, dictionary: "Dictionary", grid: Iterator[Iterator[str]]):
        self._dictionary = dictionary
        self._cells = collections.defaultdict(dict)

        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                self.set(x, y, col)

    def __getitem__(self, x: int) -> Cell:
        return self._cells[x]

    def set(self, x: int, y: int, letter: str) -> None:
        self._cells[x][y] = Cell(x, y, letter.lower())

    def size(self) -> int:
        """Returns the (rows, cols) size of the grid."""

        # Assumes that (a) all rows in the grid have the same length and (b) there
        # are no gaps (e.g. row 0 and 2 present, but 1 missing). In other words: we
        # expect set_rows() to have been properly used to set all the cells.
        nrows = max(self._cells.keys())
        ncols = max(next(iter(self._cells.values())).keys())
        return nrows + 1, ncols + 1

    def is_inside(self, x: int, y: int) -> bool:
        """Check whether (x, y) falls within the grid."""
        try:
            _ = self[x][y]
            return True
        except KeyError:
            return False

    def neighbors(self, x: int, y: int, visited: Set[Cell]) -> Iterator[Cell]:
        """Return all not-yet-visited contiguous cells."""

        for dx, dy in itertools.product([-1, 0, 1], repeat=2):
            # If both offsets are zero we remain at the same cell.
            if (dx, dy) == (0, 0):
                continue

            nx, ny = x + dx, y + dy
            if not self.is_inside(nx, ny):
                continue

            n = self[nx][ny]
            if n not in visited:
                yield n

    def find_longest_word_anywhere(self) -> str:
        """Return the longest word starting from any cell."""

        # Write your solution here.

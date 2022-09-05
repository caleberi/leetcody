"""
exercise: 1656. Design an Ordered Stream
https://leetcode.com/problems/design-an-ordered-stream/
company: Bloomberg
"""


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*n 
        self.pointer = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id-1] = value # store pair for extraction

        ans = []
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            ans.append(self.stream[self.pointer])
            self.pointer+=1
        return ans
if __name__ == '__main__':
    os = OrderedStream(5)

    assert os.insert(3, "ccccc").__eq__([])
    assert os.insert(1, "aaaaa").__eq__(['aaaaa'])
    assert os.insert(2, "bbbbb").__eq__(["bbbbb", "ccccc"])
    assert os.insert(5, "eeeee").__eq__([])
    assert os.insert(4, "ddddd").__eq__(["ddddd", "eeeee"])
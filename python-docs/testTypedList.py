import unittest
from advance_python  import TypedList


class TestTypedList(unittest.TestCase):
    def setup(self):
        self.llist = TypedList([1,2,3,4,5,6],1)

    def testGetItem(self):
        self.assertEqual(self.llist[1],5)

    def testSetItem(self):
        self.llist[2] = 8
        self.assertEqual(self.llist[2],8)


if __name__ == "__main__":
    unittest.main()

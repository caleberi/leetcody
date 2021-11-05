class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value < value:
            if self.left is None:
                self.left = Tree(value)
            return self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            return self.right.insert(value)


def pre_order_built(array):
    pass

        
from collections import deque


def level_order_traversal(tree):
    result = []
    return level_order_traversal_helper(tree,result)
    
class Tree:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.val < value:
            if self.left is None:
                self.left = Tree(value)
                return
            return self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
                return
            return self.right.insert(value)


def level_order_traversal(tree):
    return level_order_traversal_helper(tree)

def level_order_traversal_helper(root):
    if  not root :
        return []
    queue = deque([root])
    res = []
    while len(queue):
        level = []
        size = len(queue)
        while size:
            curr_node = queue.popleft()
            level.append(curr_node.val)
            size-=1
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        res.append(level)
    return res

def build_tree(vals):
    if len(vals)==0:
        return None
    root = Tree(vals[0])
    for i in range(1,len(vals)):
        root.insert(vals[i])
    return root


if __name__ == "__main__":
    tree = build_tree([1,3,2,5,6,7])
    print(level_order_traversal(tree))
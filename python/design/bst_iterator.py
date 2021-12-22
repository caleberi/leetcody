"""
Implement the BSTIterator class that represents an iterator over the in-order traversal 
of a binary search tree (BST):

- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
  The root of the BST is given as part of the constructor. 
- The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, 
otherwise returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() 
will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is,
there will be at least a next number in the in-order traversal when next() is called.


"""

POINTER_INITIAL_VALUE = -1000000


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        self.root = root
        self.pointer = TreeNode(POINTER_INITIAL_VALUE)
       
    def in_order(self,root):
        if root is None:
            return
        self.in_order(root.left)
        if self.hasNext():
            yield root
        self.in_order(root.right)

    def next(self):
        if self.root is None:
            return self.pointer
        return self.in_order(self.root)


    def hasNext(self):
        return self.root and self.root.right is not None
            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
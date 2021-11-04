class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lexicographically_smallest_leaf_to_root_path(root:Tree):
    k=move(root,[])
    k.append(root.val)
    return k

def get_smallest_child(left,right):
    if left is None and right is None:
        return None
    if left is None and right is not None:
        return right
    if right is None and left is not None:
        return left
    return left if left.val <= right.val else right


def move(root,n_list):
    if root is None:
        return n_list
    next_root = get_smallest_child(root.left,root.right)
    n_list = move(next_root,n_list)
    if next_root is not None:
        n_list.append(next_root.val)
    return n_list
        

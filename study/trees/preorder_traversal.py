def preorder_traversal(tree):
    result = []
    return preorder_traversal_helper(tree,result)

def search_in_tree_helper(tree,result):
    if tree is None:
        return result
    result.append(tree.val)
    preorder_traversal_helper(tree.left,result)
    preorder_traversal_helper(tree.right,result)
    return result
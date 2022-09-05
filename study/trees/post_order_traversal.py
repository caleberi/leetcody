def post_order_traversal(tree):
    result = []
    return post_order_traversal_helper(tree,result)

def post_order_traversal_helper(tree,result):
    if tree is None:
        return result
    post_order_traversal_helper(tree.left,result)
    post_order_traversal_helper(tree.right,result)
    result.append(tree.val)
    return result
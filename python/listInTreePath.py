def listInTreePath(root, head):
    if head is None or root is None:
        return False
    headCheck = head and head.next is None
    treeCheck = root and root.left is None and root.right is None
    if headCheck and treeCheck:
        if root.val == head.val:
            return True
        return False
    return listInTreePathHelper(root, head)


def listInTreePathHelper(root, head):
    queue = [root]  # [1]
    while len(queue):
        currentNode = queue.pop(0)
        if currentNode and currentNode.left:
            queue.append(currentNode.left)
        if currentNode and currentNode.right:
            queue.append(currentNode.right)
        if dfs(currentNode, head):
            return True
    return False


def dfs(tree, head):
    if tree is not None and head is None:
        return True
    if tree is None and head is not None:
        return False
    if tree and head and tree.val == head.val:
        # since that value are equal, look head for the next value possible
        # direction on the tree using the next element in the list
        if tree and tree.left and head and head.next:
            if tree.left.val == head.next.val:
                return dfs(tree.left, head.next)
        if tree and tree.right and head and head.next:
            if tree.right.val == head.next.val:
                return dfs(tree.right, head.next)
    else:
        return False

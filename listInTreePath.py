def listInTreePath(root, head):
    if head is None or root is None:
        return False
    if head and head.next is None and root and root.left is None and root.right is None:
        if root.value == head.value:
            return True
        return False
    return listInTreePathHelper(root, head)


def listInTreePathHelper(root, head):
    if head is None or root is None:
        return True

    queue = [root]
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
    if tree is None:
        return True

    if tree.value == head.value:
        return True
    if tree and tree.left:
        return dfs(tree.left, head.next)
    if tree and tree.right:
        dfs(tree.right, head.next)
    return False

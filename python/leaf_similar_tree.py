
def leafSimilar(root1, root2):
    def isLeaf(tree):
        return tree and tree.left is None and tree.right is None

    def bfs(root, result):
        queue = [root]
        while len(queue):
            curr = queue.pop()
            if curr and curr.left:
                queue.append(curr.left)
            if curr and curr.right:
                queue.append(curr.right)
            if isLeaf(curr):
                result.append(curr.val)
        return result
    root1_result = bfs(root1, [])
    root2_result = bfs(root2, [])
    return root1_result == root2_result

def isSameTree(p, q):
    def dfs(tree, vals):
        if tree is None:
            vals.append(None)
            return vals
        vals.append(tree.val)
        dfs(tree.left, vals)
        dfs(tree.right, vals)
        return vals
    p_arr = dfs(p, [])
    q_arr = dfs(q, [])
    return p_arr == q_arr

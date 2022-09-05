class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root:TreeNode,cnt:List[int],val:int):
            if root:
                goodNodesHelper(root.left,cnt,max(val,root.val))
                goodNodesHelper(root.right,cnt,max(val,root.val))
                if root.val >= val:
                    cnt[0]+=1
        if not root:
            return 0
        cnt = [0]
        goodNodesHelper(root,cnt,root.val)
        return cnt[0]
        

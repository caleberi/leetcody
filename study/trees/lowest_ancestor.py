from study.trees.deserialize_serialize_tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return lowestCommonAncestor(root,p,q)
    
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
        return None
    parentHistory = {}
    buildParentHistory(root,parentHistory)
    return lowestCommonAncestorHelper(root,p,q,parentHistory)

def findTreeNodeDistanceFromParent(tree:'TreeNode',node:'TreeNode'):
    return findTreeNodeDistanceFromParentHelper(tree,node,0)

def findTreeNodeDistanceFromParentHelper(tree,node,distance):
    if tree is None:
        return 0
    if tree.val == node.val:
        return distance
    left=findTreeNodeDistanceFromParentHelper(tree.left,node,distance+1)
    right=findTreeNodeDistanceFromParentHelper(tree.right,node,distance+1)
    return left+right

    

def buildParentHistory(root,history,parent=None):
    if root is None:
        return 
    history[root.val] = parent
    buildParentHistory(root.left,history,root)
    buildParentHistory(root.right,history,root)




def lowestCommonAncestorHelper(root:'TreeNode',p:'TreeNode',q:'TreeNode',history:dict) -> 'TreeNode':
    offset_p = findTreeNodeDistanceFromParent(root,p)
    offset_q = findTreeNodeDistanceFromParent(root,q)

    nodeToMove = q if offset_q > offset_p else p
    constantNode = p if nodeToMove is q else q
    distanceOffsetDifference = abs(offset_p-offset_q)
    while distanceOffsetDifference:
        nodeToMove = history[nodeToMove.val]
        distanceOffsetDifference-=1

    while constantNode != nodeToMove and constantNode is not None and nodeToMove is not None:
        nodeToMove = history[nodeToMove.val]
        constantNode = history[constantNode.val]

    if constantNode == nodeToMove:
        return constantNode
    return None

    
    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        queue = [root]
        ret = []
        while len(queue):  # while there is something in the queu
            level = len(queue)  # monitor level
            avg = getAverage(0, queue, level)
            ret.append(avg)
            idx = 0
            while idx < level:
                currentNode = queue[idx]
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)
                idx += 1
            idx = 0
            while idx < level and len(queue):
                queue.pop(0)
                idx += 1
        return ret


def getAverage(idx, queue, level):
    average = 0
    while idx < level:
        average += queue[idx].val
        idx += 1
    return average/level

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNumberHelper(tree, result, currentNumber):
            if tree is None:
                return
            if tree and tree.left is None and tree.right is None:
                currentNumber.append(str(tree.val))
                result.append("".join(currentNumber))
                currentNumber.pop()
                return

            currentNumber.append(str(tree.val))
            sumNumberHelper(tree.left, result, currentNumber)
            sumNumberHelper(tree.right, result, currentNumber)
            currentNumber.pop()

        result = []
        sumNumberHelper(root, result, [])
        total = 0
        for r in result:
            total += int(r)
        return total

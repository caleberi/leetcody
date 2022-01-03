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


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNumberHelper(tree, result, number=0):
            if tree is None:
                return
            if tree and tree.left is None and tree.right is None:
                number *= 10
                number += tree.val
                result.append(number)
                number /= 10
                return
            number *= 10
            number += tree.val
            sumNumberHelper(tree.left, result, number)
            sumNumberHelper(tree.right, result, number)
            number /= 10

        result = []
        sumNumberHelper(root, result)
        return sum(result)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNumberHelper(tree, result, number=0):
            if tree is None:
                return
            if tree and tree.left is None and tree.right is None:
                number *= 10
                number += tree.val
                result[0] += number
                number /= 10

            number *= 10
            number += tree.val
            sumNumberHelper(tree.left, result, number)
            sumNumberHelper(tree.right, result, number)

        result = [0]
        sumNumberHelper(root, result, 0)
        return result[0]

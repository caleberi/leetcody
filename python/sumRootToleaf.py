def to_decimal(str):
    total = 0
    length = len(str)
    power = 0
    for i in range(length):
        idx = length-1-i
        total += str[idx] * (2**power)
        power += 1
    return total


def sumRootToLeaf(root):
    numbers = []
    string = []
    sumRootToLeafHelper(root, string, numbers)
    return sum(numbers)


def sumRootToLeafHelper(root, string, numbers):
    if root:
        if root and root.left is None and root.right is None:
            string.append(root.val)
            numbers.append(to_decimal(string))
            string.pop()
            return
        string.append(root.val)
        sumRootToLeafHelper(root.left, string, numbers)
        sumRootToLeafHelper(root.right, string, numbers)
        string.pop()

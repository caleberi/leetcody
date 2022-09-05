
def isSymmetric(root):
    if not root:
        return True
    left =  move(root,[],'L')
    right =  move(root,[],'R')
    return right == left
    

def move(root,result,direction):
    if root is None:
        result.append(None)
        return
    if direction == 'L':
        move(root.left,result,direction,)
        result.append(root.value)
        move(root.right,result,direction)
        return
    else:
        move(root.right,result,direction)
        result.append(root.value)
        move(root.left,result,direction)
        return
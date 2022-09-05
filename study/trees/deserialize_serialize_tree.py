
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root is None:
            return []
        
        queue = []
        queue.append(root)

        result = []

        while queue:
            size = len(queue)
            for i in range(size):
                node  =  queue.pop(0)
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
        s = ''
        for i in range(len(result)):
            data = result[i]
            if data is None:
                s+='null,'
                continue
            s+=str(data)+','
        return s


    def deserialize(self, data):
        if data == '':
            return 
        data = data.strip(',').split(',')
        d = []
        for i in range(len(data)):
            dx = data[i]
            if dx=='null':
                d.append(None)
                continue
            d.append(int(dx))
        
        data = d
        
        index = 0

        root  = TreeNode(data[index])

        queue = []
        queue.append(root)
        index += 1

        while queue:
            size = len(queue)

            for i in range(size):
                node  =  queue.pop(0)
                if data[index] != None:
                    node.left =  TreeNode(data[index])
                    queue.append(node.left)
                index+=1

                if data[index] != None:
                    node.right =  TreeNode(data[index])
                    queue.append(node.right)
                index+=1
        return root

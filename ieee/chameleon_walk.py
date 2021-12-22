class Path:
    def __init__(self,x,y,c,d):
        self.x = x
        self.y = y
        self.color = c
        self.distance = d
    

class Node:
    def __init__(self,label):
        self.label = label
        self.connections = []
        self.paths = []

    def connect_path(self,node,c,d):
        if node not in self.connections:
            self.connections.add(node)
            node.connect_junction(self)
            self.paths.append(
                Path(self,node,c,d)
            )
            node.connect_path(self,c,d)

def get_largest_C_in_K(start_node,end_node,graph):
    pass


T = int(input())

for i in range(T):
    N,M,K =  tuple(map(int,input().split(" ")))
    graph = {}
    for i in range(1,N):
        if i not in graph:
            graph[i]=Node(i)
    for i in range(1,M):
        x,y,d,c = tuple(map(int,input().split(" ")))
        if x in graph and y in graph:
            graph[x].connect_path(graph[y],c,d)
    start_node = graph[1]
    end_node = graph[N]
    get_largest_C_in_K(start_node,end_node,graph,)

    


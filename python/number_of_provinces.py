class ProvinceGraph:
    def __init__(self, n_cities):
        self.root = [i for i in range(n_cities)]
        self.rank = [1]*n_cities

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1


def find_provincial_circle(matrix):
    graph = ProvinceGraph(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] == 1:
                graph.union(i, j)

    for i in range(len(matrix)):
        graph.root[i] = graph.find(i)

    return len(set(graph.root))

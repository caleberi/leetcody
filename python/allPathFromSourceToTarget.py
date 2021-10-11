# class Solution(object):
#     def allPathsSourceTarget(self, graph):
#         paths = []
#         # visited = [False for _ in range(len(graph))]

#         def dfs(node, graph, paths, path):
#             if node == len(graph, paths)-1:
#                 path.append(node)
#                 return path
#             neighbors = graph[node]
#             path.append(node)
#             for neighbor in neighbors:
#                 dfs(neighbor, graph, path)
#                 if node == 0:
#                     paths.append(path)
#                     path = []

#         dfs(0, graph, paths, [])
#         return paths


def allPathsSourceTarget(graph):
    paths = []
    # visited = [False for _ in range(len(graph))]

    def dfs(node, graph, paths, path):
        if node == len(graph)-1:
            path.append(node)
            paths.append(path)
            path = []
            return
        path.append(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            dfs(neighbor, graph, paths, path)
    dfs(0, graph, paths, [])
    return paths


graph = [[1, 2], [3], [3], []]

print(allPathsSourceTarget(graph))

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]


print(allPathsSourceTarget(graph))

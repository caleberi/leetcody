# def lonelyMatrixCount(matrix):
#     lonelyCount = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] == 1 and checkIfCellIsLonely(matrix, i, j):
#                 lonelyCount += 1
#     return lonelyCount


# def checkIfCellIsLonely(matrix, i, j):
#     neighbors = getNeighbors(matrix, i, j)
#     for neighbors in neighbors:
#         row = neighbors[0]
#         col = neighbors[1]
#         if matrix[row][col] != 0:
#             return False
#     return True


# def getNeighbors(matrix, i, j):
#     neighbors = []
#     # up , down , left , right ,up left,
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     #   (-1, -1), (-1, 1), (1, -1), (1, 1)]
#     for dx, dy in directions:  # O(8N)
#         if not inBounds(matrix, dx, dy, i, j):
#             continue
#         neighbors.append((i+dx, j+dy))
#     return neighbors


# def inBounds(matrix, dx, dy, i, j):
#     return True if (dx+i) >= 0 and (dy+j) >= 0 and (dx+i) < len(matrix) and (dy+j) < len(matrix[j]) else False


# matrix = [
#     [1, 0, 1],
#     [0, 1, 0],
#     [0, 0, 1]
# ]

# matrix = [
#     [1, 0],
#     [0, 1]
# ]


# print(lonelyMatrixCount(matrix))
# print(getNeighbors(matrix, 1, 1))
# print([matrix[x][y] for x, y in getNeighbors(matrix, 1, 1)])


# O(N^3) time | O(N*M) space
def lonelyMatrixCount(matrix):
    lonelyCount = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and checkIfCellIsLonely(matrix, i, j):
                lonelyCount += 1
    return lonelyCount


def inBounds(matrix, i, j):
    return True if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[j]) else False


def checkIfCellIsLonely(matrix, i, j):
    row = checkIthRow(matrix, i, j)
    col = checkJthCol(matrix, j, i)
    return col and row


def checkIthRow(matrix, x, y):
    for xi in range(x+1, len(matrix)):
        if inBounds(matrix, xi, y):
            if matrix[xi][y] != 0:
                return False
    for xi in range(0, x):
        if inBounds(matrix, xi, y):
            if matrix[xi][y] != 0:
                return False

    return True


def checkJthCol(matrix, x, y):
    for yi in range(y+1, len(matrix)):
        if inBounds(matrix, x, yi):
            if matrix[x][yi] != 0:
                return False
    for yi in range(0, y):
        if inBounds(matrix, x, yi):
            if matrix[x][yi] != 0:
                return False

    return True


# matrix = [
#     [1, 0],
#     [0, 1]
# ]

matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1]
]

print(lonelyMatrixCount(matrix))

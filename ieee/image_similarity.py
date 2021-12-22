def rotate_90(matrix):
    for x in range(matrix[0]):
        for y in range(matrix[x][0]):
            matrix[y][matrix[x] - x - 1] = matrix[x][y]


def transpose_horizontal(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_temp = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_temp.append(row)

    return matrix_temp

def transpose_vertical(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_temp = []
    for j in range(rows):
        col = []
        for i in range(columns):
           col.append(matrix[i][j])
        matrix_temp.append(col)

    return matrix_temp

def flip_vertical(matrix):
    for idx in range(len(matrix)):
        matrix[idx] = list(reversed(matrix[idx]))
        # image[idx] = [1 if b == 0 else 0 for b in image[idx]]
    return matrix

def flip_horizontal(matrix):
    return list(reversed(matrix))

def rotateAntiClockWise(arr):
    N=len(arr)
    for x in range(N // 2):
        for y in  range(N - x - 1):
            temp = arr[x][y]
            arr[x][y] = arr[y][N - 1 - x]
            arr[y][N - 1 -x] = arr[N - 1 - x][N - 1 - y]
            arr[N - 1 - x][N - 1 - y] = arr[N - 1 -y][x]
            arr[N - 1 - y][x] = temp
    return arr;

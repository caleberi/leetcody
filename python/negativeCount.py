# Given an MxN matrix, which is sorted in decreasing order (row-wise and column-wise),
# return the total number of negative values in the array.
# Ex: Given the following matrix…
# matrix = [
#   [3, -1],
#   [2, -2]
#  ] , return 2 (-1 and -2 are negative).
# Ex: Given the following matrix…
# matrix = [
#   [4, 3],
#  [2, 1]
# ], return 0.


def negativeCount(matrix):
    isForward = False
    i = 0  # row
    j = len(matrix[0])-1  # column
    count = 0
    while i < len(matrix):
        if isForward:
            while j < len(matrix[i]):
                if matrix[i][j] < 0:
                    matrix[i][j] = "*"
                    count += 1
                j += 1
            i += 1
            isForward = (not isForward)
            if i < len(matrix):
                j = len(matrix[i])-1
        else:
            while j >= 0:
                if matrix[i][j] > 0:
                    break
                elif matrix[i][j] < 0:
                    matrix[i][j] = "*"
                    count += 1
                j -= 1
            i += 1
            isForward = (not isForward)
            j = 0
    return count

# def negativeCount(matrix):

#     i = 0
#     count = 0
#     while i < len(matrix):
#         j = 0
#         while j < len(matrix[i]):
#             if matrix[i][j] < 0:
#                 count += len(matrix[i]) - j
#                 break
#             j += 1
#         i += 1
#     return count


# ****************************** TESTS ******************************
if __name__ == "__main__":
    print("***** Negative Count *****")
    print("Test 1:")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix 1 ✅:", negativeCount(matrix1))
    print("Expected:", 0)
    print("Test 2:")
    matrix2 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    print("Matrix 2 ✅:", negativeCount(matrix2))
    print("Expected:", 9)
    print("Test 3:")
    matrix3 = [[1, 2, 3], [6, 4, -5], [7, 8, 9]]
    print("Matrix 3:", negativeCount(matrix3))
    print("Expected:", 1)
    print("Test 4:")
    matrix4 = [[1, -1, -2], [4, 5, -6], [7, -8, -9]]
    print("Matrix 4:", negativeCount(matrix4))
    print("Expected:", 5)
    matrix5 = [[3, -1], [2, -2]]
    print("Matrix 5:", negativeCount(matrix5))
    print("Expected:", 2)
    print("Test 6:")
    matrix6 = [[4, 3], [2, 1]]
    print("Matrix 6:", negativeCount(matrix6))
    print("Expected:", 0)

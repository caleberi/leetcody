# class NumMatrix(object):

#     def __init__(self, matrix):
#         self._matrix = matrix

#     def sumRegion(self, row1, col1, row2, col2):
#         def inBounds(row1, col1, row2, col2):
#             return False if row1 < 0 or row1 > len(self._matrix)-1 or row2 < 0 or row2 > len(self._matrix)-1 or col1 < 0 or col1 > len(self._matrix[0])-1 or col2 < 0 or col2 > len(self._matrix[0])-1 else True

#         def getRectangle(row1, col1, row2, col2):
#             values = []
#             for row in range(row1, row2+1):
#                 for col in range(col1, col2+1):
#                     values.append(self._matrix[row][col])
#             print(values)
#             return values
#         if inBounds(row1, col1, row2, col2):
#             return sum(getRectangle(row1, col1, row2, col2))
#         return None


# # Your NumMatrix object will be instantiated and called as such:
# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
#     1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(2, 1, 4, 3)
# param_2 = obj.sumRegion(1, 1, 2, 2)
# param_3 = obj.sumRegion(1, 2, 2, 4)
# print(param_1)
# print(param_2)
# print(param_3)

# matrix2 = [[1], [-7]]
# obj2 = NumMatrix(matrix2)
# param_4 = obj2.sumRegion(0, 0, 0, 0)
# param_5 = obj2.sumRegion(1, 0, 1, 0)
# param_6 = obj2.sumRegion(0, 0, 1, 0)

# print(param_4)
# print(param_5)
# print(param_6)



class NumMatrix(object):

    def __init__(self, matrix):
        self._matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        def inBounds(row1, col1, row2, col2):
            return False if row1 < 0 or row1 > len(self._matrix)-1 or row2 < 0 or row2 > len(self._matrix)-1 or col1 < 0 or col1 > len(self._matrix[0])-1 or col2 < 0 or col2 > len(self._matrix[0])-1 else True

        def getRectangle(row1, col1, row2, col2):
            values = []
            width = (col2+1)-col1
            height=(row2+1)-row1
            i,j= 0,0
            while i<=height:
                values.append(self._matrix[row][width])
            print(values)
            return values
        if inBounds(row1, col1, row2, col2):
            return sum(getRectangle(row1, col1, row2, col2))
        return None


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
    1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
param_2 = obj.sumRegion(1, 1, 2, 2)
param_3 = obj.sumRegion(1, 2, 2, 4)
print(param_1)
print(param_2)
print(param_3)

matrix2 = [[1], [-7]]
obj2 = NumMatrix(matrix2)
param_4 = obj2.sumRegion(0, 0, 0, 0)
param_5 = obj2.sumRegion(1, 0, 1, 0)
param_6 = obj2.sumRegion(0, 0, 1, 0)

print(param_4)
print(param_5)
print(param_6)

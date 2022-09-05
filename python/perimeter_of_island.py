from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                total+=self._dfs(grid, i, j, seen)
        return total

    def _isALand(self, grid: List[List[int]], x: int, y: int) -> bool:
        return grid[x][y] == 1

    def _isOutOfBound(self, grid: List[List[int]], x: int, y: int) -> bool:
        return (x > len(grid)-1 or x < 0) or (y > len(grid[0])-1 or y < 0)

    def _isBoundByWaterToPos(self, grid: List[List[int]], neighbor: tuple) -> bool:
        x, y = neighbor
        return self._isOutOfBound(grid, x, y) or (not self._isALand(grid, x, y))

    def _dfs(self, grid: List[List[int]], x: int, y: int, visited: set):
        pos = f'*{x},{y}*'
        perimeter = 0
        if self._isOutOfBound(grid, x, y) or pos in visited or not self._isALand(grid, x, y):
            return perimeter

        visited.add(pos) 
        if self._isBoundByWaterToPos(grid, (x + 1, y)):
            perimeter += 1
        if self._isBoundByWaterToPos(grid, (x - 1, y)):
            perimeter += 1
        if self._isBoundByWaterToPos(grid, (x, y + 1)):
            perimeter += 1
        if self._isBoundByWaterToPos(grid, (x, y - 1)):
            perimeter += 1

        perimeter+=self._dfs(grid, x + 1, y, visited)
        perimeter+=self._dfs(grid, x, y + 1, visited)
        perimeter+=self._dfs(grid, x - 1, y, visited)
        perimeter+=self._dfs(grid, x, y - 1, visited)
        
        return perimeter

if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    s = Solution()
    print(s.islandPerimeter(grid))

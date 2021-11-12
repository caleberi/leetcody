class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        seen = set()
        m_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    m_area=max(
                        m_area,self.maxAreaOfIslandHelper(grid,i,j,seen))
        return m_area
    
    def maxAreaOfIslandHelper(self,grid,i,j,seen,area=0):
        if  (i >= 0 and i < len(grid)) and (j>=0 and j < len(grid[i])):
            if grid[i][j]==1:
                grid[i][j]=0
                area+=1
                area+=self.maxAreaOfIslandHelper(grid,i+1,j,area) #up
                area+=self.maxAreaOfIslandHelper(grid,i-1,j,area) #down
                area+=self.maxAreaOfIslandHelper(grid,i,j+1,area) #right
                area+=self.maxAreaOfIslandHelper(grid,i,j-1,area) #left
        return  area
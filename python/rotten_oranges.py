def orangesRotting( grid):
    m = len(grid)
    n = len(grid[0])

    def is_rotten(i,j):
        return grid[i][j]==2
    
    def is_empty(i,j):
        return grid[i][j]==0

    def is_valid(i,j):
        return (i>=0 and  i<m) and (j>=0 and j<n) and not is_empty(i,j)
    
    def get_neighbour(i,j):
        neighbours = [(-1,0),(1,0),(0,-1),(0,1)]
        valid = []
        for neighbour in neighbours:
            px,py = neighbour
            x,y= px+i,py+j
            if  is_valid(x,y) and not is_rotten(x,y) :
                valid.append((x,y))
        return valid
    
    def bfs(i,j,minutes=0):
        if is_valid(i,j):
            neigbours = get_neighbour(i,j)
            for neigbour in neigbours:
                x,y=neigbour
                grid[x][y]=2
            minutes += 1 if len(neigbours) else 0
            while len(neigbours):
                x,y = neigbours.pop()
                minutes=bfs(x,y,minutes)
            neigbours = get_neighbour(i,j)
            for neigbour in neigbours:
                x,y=neigbour
                grid[x][y]=1

            return minutes
        return minutes
            
    possible_minutes = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_rotten(i,j):
                temp_minutes =  bfs(i,j)
                if temp_minutes>0:
                    possible_minutes.append(temp_minutes)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1
    return min(possible_minutes)


print(orangesRotting(
    [
        [2,1,1,1],
        [1,1,0,1],
        [0,1,1,1]
    ]
))
print(orangesRotting([
    [2,1,2],
    [1,2,1],
    [0,0,1]]
))
                
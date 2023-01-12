class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid) # row
        n = len(grid[0]) # column
        area, conn = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area += 1
                    if i > 0 and grid[i-1][j] == 1: conn += 1
                    if i < m - 1 and grid[i+1][j] == 1 : conn += 1
                    if j > 0 and grid [i][j-1] == 1: conn += 1
                    if j < n - 1 and grid[i][j+1] == 1: conn += 1
            
        return area * 4 - conn
        
# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] # Outpu: 16
# grid = [[1]] # Output: 4
# grid = [[1,0]] # Output: 4
# Solution().islandPerimeter(grid)

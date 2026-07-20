class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])


        while(k):
            new_grid = [ [0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if (i != m - 1 and j == n - 1):
                        new_grid[i+1][0] = grid[i][j]
                    elif i == m - 1 and j == n - 1:
                        new_grid[0][0] = grid[m - 1][n - 1]
                    else:
                        new_grid[i][j + 1] = grid[i][j]
            grid = new_grid

            k -= 1
        return grid  

            

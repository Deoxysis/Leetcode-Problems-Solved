class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        server_rows = [0] * m
        server_cols = [0] * n

        for x in range(m):
            for y in range(n):

                if grid[x][y] == 1:
                    server_rows[x] += 1
                    server_cols[y] += 1

        comm_servers = 0

        for x in range(m):
            for y in range(n):

                if grid[x][y] == 1:

                    if server_rows[x] > 1 or server_cols[y] > 1:
                        comm_servers += 1
        return comm_servers
                

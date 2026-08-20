class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        rows = len(grid)
        cols = len(grid[0])

        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(rows))
                    for j in range(cols)]

        total_sum = sum(row_sums)

        prefix = 0
        for i in range(rows - 1):   # cut must leave both parts non-empty
            prefix += row_sums[i]
            if 2 * prefix == total_sum:
                return True
        prefix = 0
        for j in range(cols - 1):
            prefix += col_sums[j]
            if 2 * prefix == total_sum:
                return True

        return False
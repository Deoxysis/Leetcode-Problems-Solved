class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        # swap rows inside k x k submatrix
        for i in range(x, x + k // 2):
            opposite_row = 2 * x + k - 1 - i

            for j in range(y, y + k):
                grid[i][j], grid[opposite_row][j] = grid[opposite_row][j], grid[i][j]

        return grid
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        run_prod = 1
        prefix = list()
        for i in range(len(grid)):
            row_ = list()
            for j in range(len(grid[0])):
                row_.append(run_prod)
                run_prod *= grid[i][j]
                run_prod %= 12345
            prefix.append(row_)
        
        run_prod = 1
        suffix = list()
        for i in range(len(grid) - 1, -1, -1):
            row_ = list()
            for j in range(len(grid[0]) - 1, -1 , -1):
                row_.insert(0, run_prod)
                run_prod *= grid[i][j]
                run_prod %= 12345
            suffix.insert(0, row_)

        prod_mat = list()
        for i in range(len(grid)):
            row_ = list()
            for j in range(len(grid[0])):
                row_.append((prefix[i][j] * suffix[i][j]) % 12345)
            prod_mat.append(row_)
        return prod_mat
        

        # consider
        # a b c
        # d e f

        # for e, we have a*b*c*d and f, we need a*b*c*d*f
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        #start at 'S'
        #end at 'E'
        # directions up - left - up left
        # X is an obstacle
        MOD = 10**9 + 7
        ans = [0,0]
        n = len(board)
        dp = [[-9999 for col in range(n)] for row in range(n)]
        dp[-1][-1] = 0

        #fill out the bottom row and right column
        for i in range(n - 2, -1, -1):
            val = board[-1][i] #current val
            if val == 'X':
                break
            dp[-1][i] = int(val) + dp[-1][i + 1]
        
        for i in range(n - 2, -1, -1):
            val = board[i][-1] #current val
            if val == 'X':
                break
            dp[i][-1] = int(val) + dp[i + 1][-1]
        
        #fill out dp
        for r in range(n - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                if board[r][c] in 'EX': continue

                best = max(
                    [x for x in [dp[r+1][c], dp[r][c+1], dp[r+1][c+1]] if x != -9999 ], default = -9999
                )
                if best != -9999:
                    dp[r][c] = int(board[r][c]) + best
        
        dp[0][0] = max( [dp[1][0], dp[1][1],dp[0][1]] )

        ans[0] = max(dp[0][0],0) #first part done

        # how many ways to reach 0,0 ?
        # also dp

        ways = [[0 for col in range(n)] for row in range(n)]
        ways[-1][-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                if board[i][j] == 'X' or dp[i][j] == -9999:
                    continue

                val = 0 if board[i][j] in "SE" else int(board[i][j])
                prev = dp[i][j] - val

                for ni, nj in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if ni < n and nj < n and dp[ni][nj] == prev:
                        ways[i][j] += ways[ni][nj]
                        if ways[i][j] >= MOD:
                            ways[i][j] -= MOD
        
        ans[1] = ways[0][0]

        return ans

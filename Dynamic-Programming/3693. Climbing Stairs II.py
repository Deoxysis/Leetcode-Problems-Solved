class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # can only jump +1 +2 or +3
        min_costs = [10**9] * (n+1)
        min_costs[0] = 0
        for i in range(n):
            for j in range(1,4):
                if (i+j) < (n + 1):
                    min_costs[i+j] = min(min_costs[i+j], costs[i+j-1] + j**2 + min_costs[i])

        return min_costs[-1]

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_cost = 0
        cost.sort()
        counter = 0
        for i in range(len(cost) - 1, -1, -1):
            candy = cost[i]
            counter += 1
            if counter%3 != 0:
                min_cost += candy

        return min_cost
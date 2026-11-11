class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1+cost2 < costBoth:
            return cost1*need1+cost2*need2
        
        cost = min(need1,need2) * costBoth 
        
        if need1> need2:
            if cost1 < costBoth:
                cost += (need1-need2) * cost1
            else:
                cost += (need1-need2) * costBoth
        else:
            if cost2 < costBoth:
                cost += (need2-need1) * cost2
            else:
                cost += (need2-need1) * costBoth
        return cost

        

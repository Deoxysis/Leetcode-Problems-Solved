class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #intervals are of form [a,b]
        intervals.sort( key = lambda y: (y[0], -y[1]))
        max_val = -1
        count = 0
        for i in intervals:
            if i[1] > max_val:
                max_val = max(max_val, i[1])
                count += 1
        
        return count


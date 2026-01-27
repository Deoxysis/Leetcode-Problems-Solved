class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
    # n + 2 gives height, m + 2 gives width
        hBars.sort()
        vBars.sort()
        max_consecutive_h = 1
        max_consecutive_v = 1
        l1 = len(hBars)
        l2 = len(vBars)
        i = 0
        while(i < l1 - 1):
            consecutive = 1
            while ((i < l1 - 1) and (hBars[i] == hBars[i + 1] - 1)):
                consecutive += 1
                i += 1
            if consecutive > max_consecutive_h : max_consecutive_h = consecutive
            if consecutive == 1 : i += 1
        i = 0
        while(i < l2 - 1):
            consecutive = 1
            while ((i < l2 - 1) and (vBars[i] == vBars[i + 1] - 1)):
                consecutive += 1
                i += 1
            if consecutive > max_consecutive_v : max_consecutive_v = consecutive
            if consecutive == 1 : i += 1
        
        min_consecutive = min(max_consecutive_h, max_consecutive_v)
        print(min_consecutive, max_consecutive_h, max_consecutive_v)
        return (min_consecutive + 1)**2        


        
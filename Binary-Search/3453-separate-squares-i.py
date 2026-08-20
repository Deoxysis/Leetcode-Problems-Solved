class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_below(y, squares):
            above = 0
            below = 0
            for i in range(len(squares)):
                x1,y1,l = squares[i]
                if y >= y1 + l:
                    below += l * l
                elif y <= y1:
                    above+= l *l
                else:
                    below += l * abs(y - y1)
                    above += l * abs(l - y + y1)
            diff = (above - below)
            if diff == 0:
                return 0
            elif diff > 0:
                return 1
            else:
                return -1

        below = min(row[1] for row in squares)
        upper = max((row[1] + row[2]) for row in squares)
        y = float()
        y = (below+upper)/2.0
        while(upper - below > 10e-6):
            res = area_below(y, squares)
            if res == 1:
                below = y 
                y = (upper + below)/2.0
            else: 
                upper = y
                y = (upper + below)/2.0
        min_diff = 1000
        ymin = 0
        for i in range(len(squares)):
            y1, l = squares[i][1], squares[i][2]
            if y >= y1 and y<= y1+l:
                return y
            if y > y1+l and y - (y1+l) < min_diff:
                min_diff = y - (y1+1)
                ymin = y1+l

        return ymin
    
    
            


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        u = 0
        for i in moves:
            if i == 'R':
                r += 1
            elif i =='L':
                r -= 1
            elif i == 'U':
                u += 1
            else:
                u -= 1
        if u == 0 and r ==0:
            return True
        else: return False
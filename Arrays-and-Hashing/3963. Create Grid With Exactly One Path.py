class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        #first row remains .
        # last col remains .

        ans = list()
        
        temp = list()
        for i in range(n):
            temp.append('.')
        ans.append("".join(temp))

        for i in range(1,m):
            temp = []
            for j in range(n):
                if j!= n-1:
                    temp.append('#')
                else:
                    temp.append('.')
            ans.append("".join(temp))

        return ans

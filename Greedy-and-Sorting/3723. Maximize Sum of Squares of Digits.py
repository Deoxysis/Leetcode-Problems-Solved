class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = []

        while sum > 9 and num > 0:
            ans.append(9)

            sum -= 9
            num -=1
        while num > 0:
            ans.append(sum)
            sum = 0
            num -= 1
            
        if sum != 0:
            return ""
        
        return "".join(map(str,ans))

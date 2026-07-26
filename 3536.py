class Solution:
    def maxProduct(self, n: int) -> int:
        temp = list(str(n))
        temp = [int(i) for i in temp]
        temp.sort(reverse=True)
        return temp[0]*temp[1]
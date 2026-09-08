class Solution:
    def countCommas(self, n: int) -> int:
        temp = n
        l = 0
        while(temp!=0):
            l +=1
            temp //= 10
        
        #n <= 100 000
        if l < 4: return 0
        
        if l < 7: return n - 10**3 + 1


        return -1
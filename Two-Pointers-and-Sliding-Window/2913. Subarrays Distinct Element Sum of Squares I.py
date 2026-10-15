class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l = 0
        r= 0 
        n = len(nums)
        ans = 0
        for l in range(n):
            seen  = set()
            for r in range(l, n):
                seen.add(nums[r])
                ans += len(seen)**2
        
        return  ans

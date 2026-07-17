class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_val = 0
        n = len(nums)
        prefix = [0] * n

        for i,val in enumerate(nums):
            max_val = max(max_val, val)
            prefix[i] = gcd(val, max_val)
        
        prefix.sort()
        ans = 0
        for i in range(n//2):
            small = prefix[i]
            large = prefix[n - i - 1]
            ans += gcd(small, large)
        return ans
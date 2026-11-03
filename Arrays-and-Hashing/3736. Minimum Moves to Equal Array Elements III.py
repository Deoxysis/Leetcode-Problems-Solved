class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        m = max(nums)

        ans = 0
        for v in nums:
            ans += m-v
        return ans

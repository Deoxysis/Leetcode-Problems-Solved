class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        if len(nums) == 1: return 0
        nums.sort()

        median = -1
        if len(nums)%2 == 0:
            median = round((nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2)
            
        else:
            median =nums[ len(nums) // 2]

        ans = 0

        for val in nums:
            ans += abs(median - val)
        return ans

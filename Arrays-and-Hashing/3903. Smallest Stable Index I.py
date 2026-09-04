class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_found, min_found = list(), [-1 for i in range(len(nums))]
        
        rax = nums[0]
        for val in nums:
            rax = max(rax, val)
            max_found.append(rax)
        
        rax = 10**9+1
        for i in range(len(nums)-1, -1, -1):
            rax = min(rax, nums[i])
            min_found[i] = rax
        
        for i in range(len(nums)):
            diff = max_found[i] - min_found[i]
            if diff <= k:
                return i
        return -1
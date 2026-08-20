class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        c = Counter(nums)

        # Case 1: Subarrays of size 1
        if k == 1:
            valid = [num for num, count in c.items() if count == 1]
            return max(valid) if valid else -1

        # Case 2: Subarray is the entire array
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n
        maxval = -1
        if c[nums[0]] == 1:
            maxval = max(maxval, nums[0])
        if c[nums[-1]] == 1:
            maxval = max(maxval, nums[-1])

        return maxval

        

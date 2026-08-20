class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        seq = 0
        i = 1
        while i < n - 1:
            count = 2
            while i < n - 1 and (nums[i + 1] - nums[i]) == (nums[i] - nums[i - 1]):
                count += 1
                i += 1
            if count >= 3:
                count -= 2
                seq += (count * (count + 1)) // 2
            i += 1
        return seq
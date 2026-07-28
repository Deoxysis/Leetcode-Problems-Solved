class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for val in nums:
            if val > first:
                second = first
                first = val
            elif val > second:
                second = val
        return (first - 1) * (second - 1)
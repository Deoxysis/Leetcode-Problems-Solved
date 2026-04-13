class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                min_dist = min(abs(start - i), min_dist)
        return min_dist
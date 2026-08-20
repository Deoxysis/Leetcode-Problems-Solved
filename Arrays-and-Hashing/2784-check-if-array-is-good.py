class Solution:
    def isGood(self, nums: List[int]) -> bool:
        new_nums = sorted(nums)
        max_val = new_nums[-1]
        if max_val >= len(nums): return False
        c = 1
        for i in range(0, len(new_nums)-1):
            if new_nums[i] != c:
                return False
            c += 1
        if new_nums[-1] == c - 1:
            return True
        return False
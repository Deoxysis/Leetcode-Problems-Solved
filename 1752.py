class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)
        for i in range(0,len(nums)):
            spliced_arr = nums[i:] + nums[0:i]
            if spliced_arr == sorted_arr:
                return True
        return False
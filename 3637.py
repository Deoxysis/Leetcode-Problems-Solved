class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        l = len(nums)
        while i < len(nums) - 1 and nums[i] < nums[i + 1]:
            i += 1
        if i >= len(nums) - 1: return False

        if i > 0:
            
            flag = 0
            if i < len(nums) - 1 and nums[i] > nums[i + 1]: flag = 1
            while i < len(nums) - 1 and nums[i] > nums[i + 1]:
                i += 1
            if i >= len(nums) - 1: return False

            if flag == 1:
                while i < len(nums) - 1 and nums[i] < nums[i + 1]:
                    i += 1
                if i < len(nums) - 1: return False
        if i == len(nums) - 1: return True
        else: return False

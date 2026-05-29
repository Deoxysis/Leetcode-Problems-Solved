class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_digits(x):
            sums = 0
            temp = x
            while temp != 0:
                d = temp % 10
                sums += d
                temp //= 10
            return sums
        
        for i in range(len(nums)):
            nums[i] = sum_digits(nums[i])
        nums.sort()
        return nums[0]
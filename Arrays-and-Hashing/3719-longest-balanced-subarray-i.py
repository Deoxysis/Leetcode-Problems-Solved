class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxl = 0
        j = 0
        while j < len(nums):
            i = j
            temp = 0
            odd = set()
            even = set()
            while i < len(nums):
                if nums[i] % 2 == 0:
                    even.add(nums[i])
                else:
                    odd.add(nums[i])
                if len(odd) == len(even):
                    temp = i - j + 1
                i += 1
            maxl = max(maxl, temp)
            j += 1
        return maxl
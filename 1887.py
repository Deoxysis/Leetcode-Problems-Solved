class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        curr = nums[0]
        temp = 0
        ans = 0
        for i in nums:
            if i != curr:
                temp += 1
                curr = i
            ans += temp
        return ans
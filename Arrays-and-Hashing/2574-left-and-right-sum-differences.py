class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = list()
        leftsum.append(0)
        for i in range(1,len(nums)):
            leftsum.append(leftsum[i - 1] + nums[i - 1])
        rightsum = [0 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            rightsum[i] = rightsum[i + 1] + nums[i + 1]
        ans = list()
        for i in range(len(nums)):
            ans.append(abs(leftsum[i] - rightsum[i]))
        return ans


            
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        large = max(nums)
        small = min(nums)
        arr = set(nums)
        ans = list()

        for i in range(small, large+1, 1):
            if i not in arr:
                ans.append(i)
        return ans
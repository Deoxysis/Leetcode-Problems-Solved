class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i, j in enumerate(nums):
            if j in hashset:
                return True
            hashset.add(j)
        return False


# another solution is sorting (nlogn)

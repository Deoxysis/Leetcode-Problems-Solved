class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n >= 3:
            return 2**(n.bit_length() )
        elif n == 2:
            return 2
        else:
            return 1 
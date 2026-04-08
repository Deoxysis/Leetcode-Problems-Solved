class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            idx = q[0]
            while idx <= q[1]:
                nums[idx] = (nums[idx] * q[3]) % (1e9 + 7)
                idx += q[2]
        
        xors = 0
        for i in nums:
            xors ^= int(i)
        return xors
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = list()
        for n in nums:
            if n < 10:
                ans.append(n)
            else:
                n = str(n)
                for d in n:
                    ans.append(int(d))
            
        return ans
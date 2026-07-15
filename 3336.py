MOD = 10**9 + 7
import math
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)
        
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1 # Base case: empty sequences

        for x in nums:
            # a blank slate for the current number
            new_dp = [[0] * (m + 1) for _ in range(m + 1)]
            
            # Iterate through the current valid states in dp
            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    if dp[g1][g2] > 0:
                        count = dp[g1][g2]
                        
                        
                        # 1 Skip (state stays g1, g2)
                        new_dp[g1][g2] = (new_dp[g1][g2] + count % MOD)
                        # 2 Add x to seq1 (state becomes gcd(g1, x), g2)
                        new_dp[math.gcd(g1,x)][g2] = (new_dp[math.gcd(g1,x)][g2] + count) % MOD
                        # 3 Add x to seq2 (state becomes g1, gcd(g2, x))
                        new_dp[g1][math.gcd(x,g2)] = (new_dp[g1][math.gcd(x,g2)] + count) % MOD
            # Update dp for the next number in nums
            dp = new_dp
        ans = 0
        for i in range(1, m + 1):
            ans = (ans + dp[i][i]) % MOD
        return ans


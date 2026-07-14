# Last updated: 7/14/2026, 9:22:18 PM
1from math import gcd
2class Solution:
3    def subsequencePairCount(self, nums: List[int]) -> int:
4        MOD = 10**9 + 7
5        m = max(nums)
6        dp = [[0] * (m + 1) for _ in range(m + 1)]
7        dp[0][0] = 1
8        for x in nums:
9            next_dp = [row[:] for row in dp]
10            for g1 in range(m + 1):
11                for g2 in range(m + 1):
12                    if not dp[g1][g2]: continue
13                    n1, n2 = gcd(g1, x), gcd(g2, x)
14                    # add x to S1
15                    next_dp[n1][g2] = (next_dp[n1][g2] + dp[g1][g2]) % MOD
16                    # add x to S2
17                    next_dp[g1][n2] = (next_dp[g1][n2] + dp[g1][g2]) % MOD
18            dp = next_dp
19        return sum(dp[g][g] for g in range(1, m + 1)) % MOD
# Last updated: 7/10/2026, 9:09:41 PM
1class Solution:
2    def maxRepeating(self, sequence: str, word: str) -> int:
3        n = len(sequence)
4        m = len(word)
5        dp = [0] * (n + 1)
6        for i in range(m, n + 1):
7            if sequence[i-m:i] == word:
8                dp[i] = dp[i - m] + 1
9        return max(dp)
10
11        
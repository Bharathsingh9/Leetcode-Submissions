# Last updated: 8/9/2026, 8:10:42 PM
1class Solution:
2    def stoneGameII(self, piles: List[int]) -> int:
3        n = len(piles)
4        suffix = [0] * (n + 1)
5        for i in range(n - 1, -1, -1):
6            suffix[i] = suffix[i + 1] + piles[i]
7        memo = {}
8        def dp(i, M):
9            if i >= n:
10                return 0
11            if 2 * M >= n - i:
12                return suffix[i]
13            if (i, M) in memo:
14                return memo[(i, M)]
15            best = 0
16            for X in range(1, 2 * M + 1):
17                opponent = dp(i + X, max(M, X))
18                current = suffix[i] - opponent
19                best = max(best, current)
20            memo[(i, M)] = best
21            return best
22        return dp(0, 1)
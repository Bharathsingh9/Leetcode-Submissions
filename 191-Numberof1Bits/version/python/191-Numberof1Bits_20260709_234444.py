# Last updated: 7/9/2026, 11:44:44 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        res = 0
4
5        for i in range(32):
6            if (n >> i) & 1:
7                res += 1
8
9        return res
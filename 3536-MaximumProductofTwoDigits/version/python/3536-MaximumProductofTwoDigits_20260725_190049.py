# Last updated: 7/25/2026, 7:00:49 PM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        n=sorted(str(n))
4        return int(n[-1])*int(n[-2])
5
6        
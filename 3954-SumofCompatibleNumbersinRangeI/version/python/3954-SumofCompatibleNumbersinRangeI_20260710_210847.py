# Last updated: 7/10/2026, 9:08:47 PM
1class Solution:
2    def sumOfGoodIntegers(self, n: int, k: int) -> int:
3        result = 0
4
5        for x in range(max(1, n - k), n + k + 1):
6            if (n & x) == 0:
7                result += x
8
9        return result
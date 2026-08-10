# Last updated: 8/10/2026, 7:26:28 PM
1class Solution:
2    def addDigits(self, num: int) -> int:
3        while num >= 10:
4            s = 0
5            while num > 0:
6                s += num % 10
7                num //= 10
8            num = s
9        return num
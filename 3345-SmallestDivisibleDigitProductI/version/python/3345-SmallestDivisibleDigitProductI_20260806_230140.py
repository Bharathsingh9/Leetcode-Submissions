# Last updated: 8/6/2026, 11:01:40 PM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        i = n
4        while True:
5            r = 1
6            for j in str(i):
7                r = r * int(j)
8            if r % t == 0:
9                return i
10            i += 1
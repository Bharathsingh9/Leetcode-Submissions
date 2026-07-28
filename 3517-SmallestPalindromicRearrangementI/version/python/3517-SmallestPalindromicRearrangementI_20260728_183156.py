# Last updated: 7/28/2026, 6:31:56 PM
1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        if len(s) == 1:
4            return s
5        n = len(s)
6        mid = n//2
7        if n%2 == 0:
8            c = sorted(s[:mid])
9            d = c[::-1]
10            return "".join(c+d)
11        elif n%2 == 1:
12            f = sorted(s[:mid])
13            g = f[::-1]
14            return "".join(f+list(s[mid])+g)
# Last updated: 8/1/2026, 8:44:55 PM
1class Solution:
2    def countValidPrefixes(self, s: str) -> int:
3        i = 0
4        j = 0
5        r = 0
6        for k in s:
7            if k == "0":
8                i+=1
9            else:
10                j+=1
11
12            if abs(i-j)<=1:
13                r+=1
14        return r
15        
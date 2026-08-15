# Last updated: 8/15/2026, 8:39:48 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        j = len(s)
4        res = float('inf')
5        for i in range(j):
6            c = i
7            for k in range(j//2):
8                a = ord(s[(k+i)%j])-ord('a')
9                b = ord(s[(j-1-k+i)%j]) - ord('a')
10                c+=min((a-b) % 26,(b-a) % 26)
11            res = min(res,c)
12        return res
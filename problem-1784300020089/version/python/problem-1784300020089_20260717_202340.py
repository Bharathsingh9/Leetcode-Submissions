# Last updated: 7/17/2026, 8:23:40 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        g = s.split()
4        c = g[::-1]
5        return " ".join(c)
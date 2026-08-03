# Last updated: 8/3/2026, 10:00:34 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        s = s.split()
4        pattern = list(pattern)
5        if len(pattern)!=len(s):
6            return False
7        g = set(zip(s, pattern))
8        return len(g) == len(set(s)) == len(set(pattern))
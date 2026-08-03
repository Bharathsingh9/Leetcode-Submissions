# Last updated: 8/3/2026, 8:39:24 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False
5        g = set(zip(s,t))
6        print(g)
7        return len(g) == len(set(s)) == len(set(t))
8        
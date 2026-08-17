# Last updated: 8/17/2026, 9:59:19 PM
1class Solution:
2    def repeatedSubstringPattern(self, s: str) -> bool:
3        n = len(s)
4        for i in range(1, n // 2 + 1):
5            if n % i == 0 and s[:i] * (n // i) == s:
6                return True
7        return False
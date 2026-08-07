# Last updated: 8/7/2026, 9:18:32 PM
1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        for i in range(len(s)):
4            if s.count(s[i]) == 1:
5                return i
6        return -1
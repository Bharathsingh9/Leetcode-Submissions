# Last updated: 7/9/2026, 9:55:11 AM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        i = 0
4        j = 0
5        last_match = 0
6        star = -1
7        while i < len(s):
8            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
9                i += 1
10                j += 1
11            elif j < len(p) and p[j] == '*':
12                last_match = i
13                star = j
14                j += 1
15            elif star != -1:
16                j = star + 1
17                i = last_match + 1
18                last_match += 1
19            else:
20                return False
21        while j < len(p) and p[j] == '*':
22            j += 1
23        return j == len(p)
24    
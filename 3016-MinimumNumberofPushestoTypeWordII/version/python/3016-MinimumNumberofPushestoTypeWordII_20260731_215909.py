# Last updated: 7/31/2026, 9:59:09 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        f = [0] * 26
4        for k in word:
5            f[ord(k) - ord('a')] += 1
6        f.sort(reverse=True)
7        r = 0
8        for i in range(26):
9            if f[i] == 0:
10                break
11            r += f[i] * (i // 8 + 1)
12        return r
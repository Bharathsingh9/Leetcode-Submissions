# Last updated: 8/8/2026, 11:26:39 PM
1class Solution:
2    def validSequence(self, word1: str, word2: str) -> List[int]:
3        n, m = len(word1), len(word2)
4        last = [-1] * m
5        j = m - 1
6        for i in range(n - 1, -1, -1):
7            if j >= 0 and word1[i] == word2[j]:
8                last[j] = i
9                j -= 1
10        res = []
11        skip = j = 0
12        for i, c in enumerate(word1):
13            if j == m:
14                break
15            if c == word2[j] or skip == 0 and (j == m - 1 or i < last[j + 1]):
16                skip += c != word2[j]
17                res.append(i)
18                j += 1
19        return res if j == m else []
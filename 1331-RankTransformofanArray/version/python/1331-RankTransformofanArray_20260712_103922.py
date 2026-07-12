# Last updated: 7/12/2026, 10:39:22 AM
1class Solution:
2    def arrayRankTransform(self, arr: list[int]) -> list[int]:
3        ranks = {}
4        rank = 1
5        for x in sorted(list(set(arr))):
6            ranks[x] = rank
7            rank += 1
8        for i in range(len(arr)):
9            arr[i] = ranks[arr[i]]
10        return arr
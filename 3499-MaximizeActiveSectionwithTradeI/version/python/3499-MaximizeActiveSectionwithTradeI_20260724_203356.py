# Last updated: 7/24/2026, 8:33:56 PM
1class Solution:
2    def maxActiveSectionsAfterTrade(self, s: str) -> int:
3        # counts of zeros in blocks
4        zeros = map(len, filter(None, s.split("1")))
5
6        # max zeros in two consecutive blocks
7        maxzeros = max(map(sum, pairwise(zeros)), default=0)
8
9        return s.count("1") + maxzeros
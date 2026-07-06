# Last updated: 7/6/2026, 11:39:25 AM
1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: (x[0], -x[1]))
4
5        count = 0
6        maxEnd = -1
7
8        for start, end in intervals:
9            if end > maxEnd:
10                count += 1
11                maxEnd = end
12
13        return count
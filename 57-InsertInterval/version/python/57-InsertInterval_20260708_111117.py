# Last updated: 7/8/2026, 11:11:17 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        intervals.append(newInterval)
4        intervals.sort()
5
6        res = [intervals[0]]
7
8        for i in range(1, len(intervals)):
9            if res[-1][1] >= intervals[i][0]:
10                res[-1][1] = max(res[-1][1], intervals[i][1])
11            else:
12                res.append(intervals[i])
13
14        return res
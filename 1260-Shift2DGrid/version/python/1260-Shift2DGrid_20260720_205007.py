# Last updated: 7/20/2026, 8:50:07 PM
1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m = len(grid)
4        n = len(grid[0])
5
6        total = m * n
7        k %= total
8
9        ans = [[0] * n for _ in range(m)]
10
11        for i in range(m):
12            for j in range(n):
13
14                # index in 1D array (before rotation)
15                oldIndex = i * n + j
16
17                # index in 1D array (after rotation)
18                newIndex = (oldIndex + k) % total
19
20                # changing from 1D back to 2D
21                newRow = newIndex // n
22                newCol = newIndex % n
23
24                ans[newRow][newCol] = grid[i][j]
25
26        return ans
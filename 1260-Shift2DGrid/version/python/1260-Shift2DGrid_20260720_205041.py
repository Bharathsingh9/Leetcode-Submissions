# Last updated: 7/20/2026, 8:50:41 PM
1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m = len(grid)
4        n = len(grid[0])
5        total = m * n
6        k %= total
7        ans = [[0] * n for _ in range(m)]
8        for i in range(m):
9            for j in range(n):
10                oldIndex = i * n + j
11                newIndex = (oldIndex + k) % total
12                newRow = newIndex // n
13                newCol = newIndex % n
14                ans[newRow][newCol] = grid[i][j]
15        return ans
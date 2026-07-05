# Last updated: 7/5/2026, 10:29:43 AM
1class Solution:
2    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
3        grid = []
4        self.dp = {}
5        for i in range(len(board)) :
6            row = list(board[i])
7            for k in range(len(row)) :
8                row[k] = -1 if row[k] == 'X' else int(row[k]) if row[k] >= '1' and row[k] <= '9' else 0
9            grid.append(row)
10        def dfsUtil(i, j) :
11            if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 :
12                return (float(-inf), float(-inf))
13            if i == len(grid)-1 and j == len(grid)-1 :
14                return (0, 1)
15            if (i, j) in self.dp :
16                return self.dp[(i, j)]
17            down = dfsUtil(i+1, j)
18            right = dfsUtil(i, j+1)
19            diagonal = dfsUtil(i+1, j+1)
20            max_sum = max(down[0], max(right[0], diagonal[0]))
21            total_paths = 0
22            total_paths += down[-1] if down[0] == max_sum else 0
23            total_paths += right[-1] if right[0] == max_sum else 0
24            total_paths += diagonal[-1] if diagonal[0] == max_sum else 0
25            self.dp[(i, j)] = [max_sum+grid[i][j], total_paths]
26            return [max_sum+grid[i][j], total_paths] 
27        max_sum, paths = dfsUtil(0, 0)
28        return [max_sum % ((10 ** 9) + 7), paths % ((10 ** 9) + 7)] if max_sum != float(-inf) else (0, 0)
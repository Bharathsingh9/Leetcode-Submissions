# Last updated: 7/10/2026, 10:03:48 AM
1inf = float('inf')
2class Solution:
3    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
4        vi = sorted([(v, i) for i, v in enumerate(nums)])
5        n2i = {t[1]: i for i, t in enumerate(vi)}
6        vals = [t[0] for t in vi]
7
8        h = len(bin(n)[2:]) + 1
9        jumps = [[-1] * h for _ in range(n)]
10        j = 0
11        for i in range(n):
12            while j+1 < n and vals[j+1] - vals[i] <= maxDiff:
13                j += 1
14            jumps[i][0] = j
15        for j in range(1, h):
16            for i in range(n):
17                jumps[i][j] = jumps[jumps[i][j-1]][j-1]
18        
19        def query(a, b, h):
20            if a == b:
21                return 0
22            if jumps[a][0] >= b:
23                return 1
24            if jumps[a][h] < b:
25                return inf 
26            for j in range(h, -1, -1):
27                if jumps[a][j] < b:
28                    break
29            return (1 << j) + query(jumps[a][j], b, j)
30            
31        
32        res = []
33        for a, b in queries:
34            a, b = n2i[a], n2i[b]
35            cur = query(min(a, b), max(a, b), h-1)
36            res.append(cur if cur < inf else -1)
37        return res
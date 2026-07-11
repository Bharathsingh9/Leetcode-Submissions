# Last updated: 7/11/2026, 10:56:16 AM
1class Solution:
2    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph = [[] for _ in range(n)]
4        
5        for u, v in edges:
6            graph[u].append(v)
7            graph[v].append(u)
8
9        visited = [False] * n
10        ans = 0
11
12        def dfs(node):
13            visited[node] = True
14            vertices.append(node)
15
16            for nei in graph[node]:
17                if not visited[nei]:
18                    dfs(nei)
19
20        for i in range(n):
21            if not visited[i]:
22                vertices = []
23                dfs(i)
24
25                k = len(vertices)
26                edge_count = sum(len(graph[v]) for v in vertices) // 2
27
28                if edge_count == k * (k - 1) // 2:
29                    ans += 1
30
31        return ans
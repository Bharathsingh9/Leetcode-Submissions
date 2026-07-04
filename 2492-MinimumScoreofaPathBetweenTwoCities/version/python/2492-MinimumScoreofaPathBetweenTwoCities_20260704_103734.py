# Last updated: 7/4/2026, 10:37:34 AM
1class Solution:
2    def minScore(self, n: int, roads: List[List[int]]) -> int:
3        graph = defaultdict(list)
4
5        for u, v, d in roads:
6            graph[u].append((v, d))
7            graph[v].append((u, d))
8
9        visited = [False] * (n + 1)
10        ans = float('inf')
11
12        q = deque([1])
13        visited[1] = True
14
15        while q:
16            node = q.popleft()
17
18            for nei, dist in graph[node]:
19                ans = min(ans, dist)
20                if not visited[nei]:
21                    visited[nei] = True
22                    q.append(nei)
23
24        return ans
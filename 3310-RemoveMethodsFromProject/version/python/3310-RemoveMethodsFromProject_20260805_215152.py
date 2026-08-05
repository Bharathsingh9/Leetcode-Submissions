# Last updated: 8/5/2026, 9:51:52 PM
1class Solution:
2    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
3        adj = {i: [] for i in range(n)}
4        for src, dst in invocations:
5            adj[src].append(dst)
6        q = [k]
7        visited = set([k])
8        while q:
9            suspicious = q.pop()
10            for neighbor in adj[suspicious]:
11                if neighbor not in visited:
12                    visited.add(neighbor)
13                    q.append(neighbor)      
14        ans = []
15        for method in range(n):
16            if method in visited: continue
17            for neighbor in adj[method]:
18                if neighbor in visited:
19                    return list(range(n))
20            ans.append(method)
21        return ans
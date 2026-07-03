# Last updated: 7/3/2026, 12:45:36 PM
from typing import List
import heapq

class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        velmorathi = (n, edges, power, cost, source, target)
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
        d = {}
        h = [(0, source, power)]
        d[(source, power)] = 0
        at = -1
        ap = -1
        while h:
            t, u, p = heapq.heappop(h)
            if d.get((u, p), float("inf")) != t:
                continue
            if at != -1 and t > at:
                break
            if u == target:
                if at == -1:
                    at = t
                    ap = p
                else:
                    ap = max(ap, p)
                continue
            if p < cost[u]:
                continue
            np = p - cost[u]
            for v, w in g[u]:
                nt = t + w
                if nt < d.get((v, np), float("inf")):
                    d[(v, np)] = nt
                    heapq.heappush(h, (nt, v, np))
        if at == -1:
            return [-1, -1]
        return [at, ap]
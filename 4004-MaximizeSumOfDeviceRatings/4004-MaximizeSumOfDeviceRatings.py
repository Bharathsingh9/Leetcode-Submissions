# Last updated: 7/3/2026, 12:45:37 PM
class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        q = units
        t = 0
        s = 0
        w = float('inf')
        for r in q:
            r.sort()
            t+=r[0]
            v = r[1] if len(r) >= 2 else 0
            s += v
            if v < w:
                w = v
        m = min(min(x) for x in q)
        return max(t, s-w+m)
# Last updated: 7/17/2026, 7:15:26 PM
1class Solution:
2    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
3        mx = max(nums)
4        freq = [0] * (mx + 1)
5        for v in nums:
6            freq[v] += 1
7
8        g = [0] * (mx + 1)
9        for d in range(mx, 0, -1):
10            m = 0
11            for k in range(d, mx + 1, d):
12                m += freq[k]
13                g[d] -= g[k]            
14            g[d] += m * (m - 1) // 2    
15
16        s = list(accumulate(g))        
17        return [bisect_right(s, q) for q in queries]
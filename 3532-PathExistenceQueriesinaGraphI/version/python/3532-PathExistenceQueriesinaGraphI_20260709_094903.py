# Last updated: 7/9/2026, 9:49:03 AM
1class Solution:
2    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
3        p = [i for i in range(n)]
4
5        for i in range(1, n):
6            if nums[i]-nums[i-1] <= maxDiff: 
7                p[i] = p[i-1]
8        
9        return [p[i] == p[j] for i,j in queries]
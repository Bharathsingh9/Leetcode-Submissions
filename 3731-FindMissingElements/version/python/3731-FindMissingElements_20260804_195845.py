# Last updated: 8/4/2026, 7:58:45 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        M = max(nums)
4        N = min(nums)
5        ans = []
6        for i in range(N,M):
7            if i not in nums:
8                ans.append(i)
9        return ans
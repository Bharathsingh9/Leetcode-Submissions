# Last updated: 7/30/2026, 12:20:25 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        maxi = float("-inf")
4        w = sum(nums[:k])
5        maxi = max(w,maxi)
6        for i in range(k,len(nums)):
7            w+=nums[i]
8            w-=nums[i-k]
9            maxi = max(w,maxi)
10        return maxi/float(k)
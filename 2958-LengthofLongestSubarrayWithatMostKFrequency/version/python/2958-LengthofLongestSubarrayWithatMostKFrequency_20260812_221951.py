# Last updated: 8/12/2026, 10:19:51 PM
1class Solution:
2    def maxSubarrayLength(self, nums, k):
3        m = {}
4        i = 0
5        res = 0
6        for j in range(len(nums)):
7            m[nums[j]] = m.get(nums[j], 0) + 1
8            while m[nums[j]] > k:
9                m[nums[i]] -= 1
10                i += 1
11            res = max(res, j - i + 1)
12        return res
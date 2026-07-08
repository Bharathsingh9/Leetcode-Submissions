# Last updated: 7/8/2026, 11:13:29 AM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        nums = [n for n in nums if n > 0]
4        nums.sort()
5
6        target = 1
7        for n in nums:
8            if n == target:
9                target += 1
10            elif n > target:
11                return target
12        
13        return target
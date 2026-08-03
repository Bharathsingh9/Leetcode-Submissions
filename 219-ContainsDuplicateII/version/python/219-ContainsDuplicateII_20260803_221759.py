# Last updated: 8/3/2026, 10:17:59 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        d = {}
4        for i in range(len(nums)):
5            if nums[i] in d and i - d[nums[i]] <= k:
6                return True
7            d[nums[i]] = i
8        return False
9
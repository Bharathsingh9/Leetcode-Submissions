# Last updated: 7/26/2026, 10:22:32 AM
1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums.sort()
4        res = max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
5        return res
6        
# Last updated: 8/5/2026, 6:54:10 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(nums) != len(set(nums))
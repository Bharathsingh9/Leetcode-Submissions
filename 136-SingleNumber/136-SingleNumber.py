# Last updated: 7/3/2026, 12:47:53 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            c=c^nums[i]
        return c
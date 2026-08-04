# Last updated: 8/4/2026, 7:55:08 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        nums.sort()
4        res = []
5        for i in range(1,len(nums)):
6            for j in range(nums[i-1]+1,nums[i]):
7                res.append(j)
8        return res
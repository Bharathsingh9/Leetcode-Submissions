# Last updated: 7/3/2026, 12:49:14 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in d:
                return [d[rem],i]
            d[num]=i
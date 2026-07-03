# Last updated: 7/3/2026, 12:47:22 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm={}
        for i in range(len(nums)):
            hm[nums[i]]=hm.get(nums[i],0)+1
        for key,values in hm.items():
            if values>1:
                return key
                
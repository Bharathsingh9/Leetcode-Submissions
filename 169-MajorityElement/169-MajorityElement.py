# Last updated: 7/3/2026, 12:47:43 PM
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        hm={}
        maxi=float("-inf")
        for i in range(len(nums)):
            hm[nums[i]]=hm.get(nums[i],0)+1
            if hm[nums[i]]>maxi:
                maxi=hm[nums[i]]
                ans=nums[i]
        if maxi>n//2:
            return ans
            




        
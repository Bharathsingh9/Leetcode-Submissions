# Last updated: 7/3/2026, 12:47:35 PM
class Solution(object):
    def majorityElement(self, nums):
        res=[]
        hm={}
        for i in range(len(nums)):
            hm[nums[i]]=hm.get(nums[i],0)+1
        maxi=float("-inf")
        ele=0
        for key in hm:
            if hm[key]>len(nums)//3:
                res.append(key)
        return res


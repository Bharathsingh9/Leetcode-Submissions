# Last updated: 7/3/2026, 12:47:19 PM
class Solution(object):
    def splitArray(self, nums, k):
        low=max(nums)
        high=sum(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            pages=0
            student=1
            for i in range(len(nums)):
                if pages+nums[i]<=mid:
                    pages+=nums[i]
                else:
                    student+=1
                    pages=nums[i]
            if student>k:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
        
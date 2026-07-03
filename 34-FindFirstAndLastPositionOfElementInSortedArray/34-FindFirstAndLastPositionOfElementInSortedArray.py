# Last updated: 7/3/2026, 12:48:33 PM
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        low=0
        high=len(nums)-1
        ans=-1
        bns=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    ans=mid
                high=mid-1
            else:
                low=mid+1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    bns=mid
                low=mid+1
            else:
                high=mid-1
        return [ans,bns]
        

        




        
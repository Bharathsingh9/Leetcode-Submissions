# Last updated: 7/3/2026, 12:47:46 PM
class Solution(object):
    def findMin(self, nums):
        ans=float("inf")
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans

        
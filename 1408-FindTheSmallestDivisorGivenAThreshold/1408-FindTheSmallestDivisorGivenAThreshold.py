# Last updated: 7/3/2026, 12:46:26 PM
from math import ceil
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        ans=high
        
        while low<=high:
            mid=(low+high)//2
            c=0
            for i in range(len(nums)):
                c += (nums[i] + mid - 1) // mid
            
            if c<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
            



        
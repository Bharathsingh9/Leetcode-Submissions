# Last updated: 7/3/2026, 12:46:12 PM
class Solution(object):
    def findKthPositive(self, arr, k):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            m=arr[mid]-(mid+1)
            if k>m:
                low=mid+1
            else:
                high=mid-1
        return high+k+1
        
        
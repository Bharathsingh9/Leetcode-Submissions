# Last updated: 7/3/2026, 12:46:54 PM

class Solution(object):
    def minEatingSpeed(self, piles, h):
        maxi=max(piles)
        low=1
        high=maxi
        ans=maxi
        while low<=high:
            mid=(low+high)//2
            totalh=0
            for p in piles:
                totalh+=(p+mid-1)//mid

            if totalh<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


        
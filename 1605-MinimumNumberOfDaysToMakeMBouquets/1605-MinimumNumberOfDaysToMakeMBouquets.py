# Last updated: 7/3/2026, 12:46:13 PM
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k>len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)

        while low<=high:
            mid=(low+high)//2
            count=0
            ans=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    count+=1
                else:
                    ans+=count//k
                    count=0
            ans+=count//k
            if ans>=m:
                high=mid-1
            else:
                low=mid+1
        return low

            
            

        
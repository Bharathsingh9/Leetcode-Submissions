# Last updated: 7/3/2026, 12:46:46 PM
class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        ans=0
        while low<=high:
            mid=(low+high)//2
            sumi=0
            count=1
            for i in range(len(weights)):
                if sumi+weights[i]<=mid:
                    sumi+=weights[i]
                else:
                    count+=1
                    sumi=weights[i]
            if count<=days:
                ans=mid 
                high=mid-1
            else:
                low=mid+1
        return ans               
        
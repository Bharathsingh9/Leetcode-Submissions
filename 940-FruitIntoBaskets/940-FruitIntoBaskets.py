# Last updated: 7/3/2026, 12:46:53 PM
class Solution(object):
    def totalFruit(self, fruits):
        hm=dict()
        maxi=0
        l=0
        k=2
        r=0
        while r<len(fruits):
            hm[fruits[r]]=hm.get(fruits[r],0)+1
            if len(hm)>k:
                hm[fruits[l]]-=1
                if hm[fruits[l]]==0:
                    del hm[fruits[l]]
                l+=1
            if len(hm)<=k:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi


        
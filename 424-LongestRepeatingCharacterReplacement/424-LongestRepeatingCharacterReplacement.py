# Last updated: 7/3/2026, 12:47:18 PM
class Solution(object):
    def characterReplacement(self, s, k):
        hm={}
        l=0
        r=0
        maxf=0
        maxl=0
        while r<len(s):
            hm[s[r]]=hm.get(s[r],0)+1
            maxf=max(maxf,hm[s[r]])
            if (r-l+1)-maxf > k:
                hm[s[l]]-=1
                l+=1
            maxl=max(maxl,r-l+1)
            r+=1
        return maxl
        
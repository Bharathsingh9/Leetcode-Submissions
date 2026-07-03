# Last updated: 7/3/2026, 12:45:59 PM
class Solution(object):
    def countGoodSubstrings(self, s):
        k=3
        count=0
        w=s[:k]
        if len(set(w))==3:
            count+=1
        for i in range(k,len(s)):
            w=w[1:]+s[i]
            if len(set(w))==3:
                count+=1
        return count


        
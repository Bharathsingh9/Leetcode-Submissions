# Last updated: 7/3/2026, 12:47:16 PM
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hm={}
        for i in range(len(s)):
            hm[s[i]]=hm.get(s[i],0)+1
        def fun(a):
            return hm[a]
        print(hm)
        a=sorted(hm,key=fun,reverse=True)
        print(a)
        r=""
        for j in range(len(a)):
            r+=a[j] * hm[a[j]]
        return r

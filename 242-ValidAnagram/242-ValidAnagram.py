# Last updated: 7/3/2026, 12:47:27 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        hm={}
        for i in range(len(s)):
            hm[s[i]]=hm.get(s[i],0)+1
        for i in range(len(t)):
            if t[i] not in hm:
                return False
            hm[t[i]]-=1
            if hm[t[i]]==0:
                del hm[t[i]]
        return len(hm)==0

        
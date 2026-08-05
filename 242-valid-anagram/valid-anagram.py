class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
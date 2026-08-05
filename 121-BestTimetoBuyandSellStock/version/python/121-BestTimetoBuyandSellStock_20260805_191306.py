# Last updated: 8/5/2026, 7:13:06 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False
5        hm={}
6        for i in range(len(s)):
7            hm[s[i]]=hm.get(s[i],0)+1
8        for i in range(len(t)):
9            if t[i] not in hm:
10                return False
11            hm[t[i]]-=1
12            if hm[t[i]]==0:
13                del hm[t[i]]
14        return len(hm)==0
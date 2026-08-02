# Last updated: 8/2/2026, 7:16:06 PM
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        hm1 = {}
4        hm2 = {}
5        for i in ransomNote:
6            hm1[i] = hm1.get(i,0)+1
7        for j in magazine:
8            hm2[j] = hm2.get(j,0)+1
9        for k in hm1:
10            if k not in hm2 or hm2[k] < hm1[k] :
11                return False
12        return True           
# Last updated: 7/11/2026, 12:58:09 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        h = {}
4        ans = []
5
6        for i in strs:
7            k = ''.join(sorted(i))
8
9            if k in h:
10                h[k].append(i)
11            else:
12                h[k] = [i]
13
14        for k, v in h.items():
15            ans.append(v)
16
17        return ans
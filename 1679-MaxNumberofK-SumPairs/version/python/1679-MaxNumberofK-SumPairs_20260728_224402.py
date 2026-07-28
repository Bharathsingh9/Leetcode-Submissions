# Last updated: 7/28/2026, 10:44:02 PM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        hm ={}
4        count = 0
5        for i in nums:
6            s = k - i
7            if s in hm and hm.get(s,0)>0:
8                hm[s]-=1
9                count+=1
10            else:
11                hm[i] = hm.get(i,0)+1
12        return count
13        
14
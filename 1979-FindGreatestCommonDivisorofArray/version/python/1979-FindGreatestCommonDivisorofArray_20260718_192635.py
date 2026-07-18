# Last updated: 7/18/2026, 7:26:35 PM
1class Solution:
2    def findGCD(self, nums: List[int]) -> int:
3        i=1
4        j=1
5        a=[]
6        b=[]
7        M = float("-inf")
8        N = float("inf")
9        for k in range(len(nums)):
10            M = max(M,nums[k])
11            N = min(N,nums[k])
12        while i<=M:
13            if M%i == 0:
14                a.append(i)
15            i+=1
16        while j<=N:
17            if N%j == 0:
18                b.append(j)  
19            j+=1
20        G = max(list(set(a) & set(b)))
21        return G
22        
23        
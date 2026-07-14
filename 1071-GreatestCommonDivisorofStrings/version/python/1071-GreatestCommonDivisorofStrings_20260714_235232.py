# Last updated: 7/14/2026, 11:52:32 PM
1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3
4        n=len(str1)
5        m=len(str2)
6        if n>m:
7            str1,str2=str2,str1
8        n=len(str1)
9        m=len(str2)
10        
11        
12        for i in range(n-1,-1,-1):
13            v = str1[:i+1]
14            g = len(v)
15            if n % g != 0 or m % g != 0:
16                continue
17            if v*(n//g) == str1 and v*(m//g) == str2:
18                return v
19        return ""
20            
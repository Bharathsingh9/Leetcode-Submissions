# Last updated: 7/30/2026, 10:23:43 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        n=len(word)
4        r=0 
5        p=1
6        while n>=8:
7            r+=(8*p)
8            p+=1
9            n-=8
10        r+=(n*p)
11        return r
12            
13            
# Last updated: 7/15/2026, 6:29:16 PM
1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        sumi=0
4        sumii=0
5        for i in range(1,n*2+1):
6            if i%2==0:
7                sumi+=i
8            else:
9                sumii+=i
10        
11        return n
12        
13
# Last updated: 8/2/2026, 11:25:50 PM
1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        for i in [2,3,5]:
6            while n%i == 0:
7                n = n//i
8        if n == 1:
9            return True
10        else:
11            return False
12        
13            
14            
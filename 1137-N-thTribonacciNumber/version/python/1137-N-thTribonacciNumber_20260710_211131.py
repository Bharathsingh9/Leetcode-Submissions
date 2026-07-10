# Last updated: 7/10/2026, 9:11:31 PM
1class Solution:
2    def tribonacci(self, n: int) -> int:
3        a = 0  
4        b = 1  
5        c = 1  
6        if n == 0:
7            return 0  
8        if n == 1 or n == 2:
9            return 1  
10        for i in range(3, n+1):  
11            d = a + b + c  
12            a = b 
13            b = c  
14            c = d  
15        return d  
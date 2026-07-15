# Last updated: 7/15/2026, 6:33:58 PM
1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        sumOdd = 0
4        sumEven = 0
5
6        for i in range(2*n+1):
7            if i % 2 == 1:
8                sumOdd += i
9            else:
10                sumEven += i
11
12        res = 0
13
14        bigger = max(sumOdd, sumEven)
15
16        for i in range(1, bigger // 2 + 1):
17            if sumOdd % i == 0 and sumEven % i == 0:
18                res = i
19        
20        return res
21        
22
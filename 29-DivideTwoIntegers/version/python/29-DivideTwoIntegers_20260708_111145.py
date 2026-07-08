# Last updated: 7/8/2026, 11:11:45 AM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        INT_MAX, INT_MIN = 2**31 - 1, -2**31
4
5        if dividend == INT_MIN and divisor == -1:
6            return INT_MAX
7
8        negative = (dividend < 0) ^ (divisor < 0)
9        a, b = abs(dividend), abs(divisor)
10        
11        quotient = 0
12
13        powers = []
14        val = b
15        while val <= a:
16            powers.append(val)
17            val <<= 1
18
19        for i in range(len(powers) - 1, -1, -1):
20            if a >= powers[i]:
21                a -= powers[i]
22                quotient += (1 << i)
23        
24        result = -quotient if negative else quotient
25
26        return max(INT_MIN, min(INT_MAX, result))
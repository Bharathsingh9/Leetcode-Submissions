# Last updated: 8/2/2026, 11:00:49 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        if n<10:
4            if n == 1 or n == 7:
5                return True
6            else:
7                return False
8        def ans(m):
9            if m<10:
10                if m == 1 or m == 7:
11                    return True
12                else:
13                    return False
14            i = 0
15            while m > 0:
16                j = m % 10
17                i += j * j
18                m = m // 10
19            if i == 1:
20                return True
21            else:
22                return ans(i)
23        return ans(n)
24        
25    
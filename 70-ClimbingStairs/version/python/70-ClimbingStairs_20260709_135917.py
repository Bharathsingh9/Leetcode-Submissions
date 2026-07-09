# Last updated: 7/9/2026, 1:59:17 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 3:
4            return n
5        prev = 3
6        prev_prev = 2
7        current = 0
8
9        for _ in range(3, n):
10            current = prev + prev_prev
11            prev_prev = prev
12            prev = current
13        
14        return current
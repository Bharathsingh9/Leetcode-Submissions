# Last updated: 7/9/2026, 9:58:32 AM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x == 0:
4            return 0
5        first, last = 1, x
6        while first <= last:
7            mid = first + (last - first) // 2
8            if mid == x // mid:
9                return mid
10            elif mid > x // mid:
11                last = mid - 1
12            else:
13                first = mid + 1
14        return last
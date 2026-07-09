# Last updated: 7/9/2026, 11:41:05 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        ans = 0
4        for _ in range(32):
5            bit = n & 1
6            ans = (ans << 1) | bit
7            n >>= 1
8        return ans
# Last updated: 7/24/2026, 8:38:58 PM
1class Solution:
2    def uniqueXorTriplets(self, nums: List[int]) -> int:
3        return n if (n:=len(nums))<3 else 1<<n.bit_length()
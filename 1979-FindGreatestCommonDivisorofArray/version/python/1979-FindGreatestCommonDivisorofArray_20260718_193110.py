# Last updated: 7/18/2026, 7:31:10 PM
1class Solution:
2    def findGCD(self, nums: List[int]) -> int:
3        return gcd(min(nums), max(nums))
4        
5        
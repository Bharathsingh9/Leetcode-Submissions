# Last updated: 7/16/2026, 6:24:48 PM
1class Solution:
2    def gcdSum(self, nums: list[int]) -> int:
3        pgcd = sorted(map(gcd, nums, accumulate(nums, max)))
4        return sum(map(gcd, islice(pgcd, len(nums) // 2), reversed(pgcd)))  
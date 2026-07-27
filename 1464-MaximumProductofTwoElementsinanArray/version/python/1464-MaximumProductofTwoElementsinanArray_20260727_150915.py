# Last updated: 7/27/2026, 3:09:15 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        first_max = float('-inf')
4        second_max = float('-inf')
5        for i in nums:
6            if i >= first_max:
7                second_max = first_max
8                first_max = i
9            elif i > second_max:
10                second_max = i
11        return (first_max-1)*(second_max-1)
12
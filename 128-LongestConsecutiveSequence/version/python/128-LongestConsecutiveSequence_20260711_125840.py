# Last updated: 7/11/2026, 12:58:40 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        longest = 0
4        num_set = set(nums)
5
6        for n in num_set:
7            if (n-1) not in num_set:
8                length = 1
9                while (n+length) in num_set:
10                    length += 1
11                longest = max(longest, length)
12        
13        return longest
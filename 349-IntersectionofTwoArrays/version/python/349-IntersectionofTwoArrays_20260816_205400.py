# Last updated: 8/16/2026, 8:54:00 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        l = []
4        n = list(set(nums1))
5        for i in range(len(n)):
6            if n[i] in nums2:
7                l.append(n[i])
8        return l
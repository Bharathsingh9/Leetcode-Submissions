# Last updated: 7/26/2026, 3:51:31 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        nums1 = list(set(nums1))
4        nums2 = list(set(nums2))
5        m = nums1.copy()
6        n = nums2.copy()
7        for i in m:
8            if i in n:
9                nums1.remove(i)
10        for k in n:
11            if k in m:
12                nums2.remove(k)
13        return nums1,nums2
14        
15
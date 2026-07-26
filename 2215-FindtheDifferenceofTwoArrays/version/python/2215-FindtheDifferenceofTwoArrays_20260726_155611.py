# Last updated: 7/26/2026, 3:56:11 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]
4        
5        
6
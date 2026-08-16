class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        n = list(set(nums1))
        for i in range(len(n)):
            if n[i] in nums2:
                l.append(n[i])
        return l
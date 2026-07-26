class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        m = nums1.copy()
        n = nums2.copy()
        for i in m:
            if i in n:
                nums1.remove(i)
        for k in n:
            if k in m:
                nums2.remove(k)
        return nums1,nums2
        

# Last updated: 7/3/2026, 12:49:10 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i=0
        j=0
        n1=len(nums1)
        n2=len(nums2)
        n=n1+n2
        c=n/2
        d=c-1
        s1=-1
        s2=-1
        cnt=0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                if cnt==d:
                    s1=nums1[i]
                if cnt==c:
                    s2=nums1[i]
                i+=1
                cnt+=1
            else:
                if cnt==d:
                    s1=nums2[j]
                if cnt==c:
                    s2=nums2[j]
                j+=1
                cnt+=1
        while i<n1:
            if cnt==d:
                s1=nums1[i]
            if cnt==c:
                s2=nums1[i]
            i+=1
            cnt+=1
        while j<n2:
            if cnt==d:
                s1=nums2[j]
            if cnt==c:
                s2=nums2[j]
            j+=1
            cnt+=1
        if n%2==1:
            return s2
        else:
            return ((s1+s2)/2.0)


        

        
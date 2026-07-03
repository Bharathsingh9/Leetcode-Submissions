# Last updated: 7/3/2026, 12:46:29 PM
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atmost(l):
            if l<0:
                return 0
            left=0
            right=0
            sumi=0
            count=0
            while right<len(nums):
                sumi+=nums[right]%2
                while sumi>l:
                    sumi-=nums[left]%2
                    left+=1
                count+=right-left+1
                right+=1
            return count
        return atmost(k)-atmost(k-1)


        
# Last updated: 7/3/2026, 12:46:48 PM
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atmost(l):
            if l<0:
                return 0
            count=0
            right=0
            left=0
            h={}
            while right<len(nums):
                h[nums[right]]=h.get(nums[right],0)+1
                while len(h)>l:
                    h[nums[left]]-=1
                    if h[nums[left]]==0:
                        del h[nums[left]]
                    left+=1
                count+=right-left+1
                right+=1
            return count
        return atmost(k)-atmost(k-1)

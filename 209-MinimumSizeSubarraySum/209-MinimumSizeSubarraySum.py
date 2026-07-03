# Last updated: 7/3/2026, 12:47:34 PM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        sumi=0
        mini=float("inf")
        for right in range(len(nums)):
            sumi+=nums[right]
            while sumi>=target:
                mini=min(mini,right-left+1)
                sumi-=nums[left]
                left+=1
        if mini==float("inf"):
            return 0
        return mini

        
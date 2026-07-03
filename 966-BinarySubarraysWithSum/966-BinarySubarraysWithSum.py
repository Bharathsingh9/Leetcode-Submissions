# Last updated: 7/3/2026, 12:46:51 PM
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atmost(k):
            if k<0:
                return 0
            left=0
            right=0
            sumi=0
            count=0
            while right<len(nums):
                sumi+=nums[right]
                while sumi>k:
                    sumi-=nums[left]
                    left+=1
                count+=right-left+1
                right+=1
            return count
        return atmost(goal)-atmost(goal-1)
                




        
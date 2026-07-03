# Last updated: 7/3/2026, 12:46:15 PM
class Solution(object):
    def longestSubarray(self, nums):
            zeroes=0
            right=0
            left=0
            k=1
            maxi=0
            while right<len(nums):
                if nums[right]==0:
                    zeroes+=1
                while zeroes>k:
                    if nums[left]==0:
                        zeroes-=1
                    left+=1

                maxi=max(maxi,right-left)
                right+=1
            return maxi

        
# Last updated: 7/3/2026, 12:48:41 PM
class Solution(object):
    def removeDuplicates(self, nums):
        slow=1
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
        return slow



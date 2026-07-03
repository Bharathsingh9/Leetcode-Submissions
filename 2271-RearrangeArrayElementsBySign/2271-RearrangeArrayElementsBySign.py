# Last updated: 7/3/2026, 12:45:51 PM
class Solution(object):
    def rearrangeArray(self, nums):
        li=[]
        gi=[]
        for i in range(len(nums)):
            if nums[i]>0:
                li.append(nums[i])
            else:
                gi.append(nums[i])
        result=[]
        for i in range(len(li)):
            result.append(li[i])
            result.append(gi[i])
        return result

        

        
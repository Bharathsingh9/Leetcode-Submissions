# Last updated: 7/3/2026, 12:47:01 PM
class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=sum(nums[:k])
        maxi=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]
            window_sum-=nums[i-k]
            maxi=max(maxi,window_sum)
        return maxi/float(k)

        
 
        
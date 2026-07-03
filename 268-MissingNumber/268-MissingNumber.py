# Last updated: 7/3/2026, 12:47:25 PM
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        ex_sum=n*(n+1)//2
        ac_sum=sum(nums)
        ans = ex_sum - ac_sum
        return ans



        
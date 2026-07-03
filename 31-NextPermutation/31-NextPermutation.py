# Last updated: 7/3/2026, 12:48:37 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = -1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx==-1:
            return nums.reverse()
        for j in range(n-1,idx,-1):
            if nums[j] >nums[idx]:
                nums[j],nums[idx]=nums[idx],nums[j]
                break
        nums[idx+1:]=nums[idx+1:][::-1]      
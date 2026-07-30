class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = float("-inf")
        w = sum(nums[:k])
        maxi = max(w,maxi)
        for i in range(k,len(nums)):
            w+=nums[i]
            w-=nums[i-k]
            maxi = max(w,maxi)
        return maxi/float(k)
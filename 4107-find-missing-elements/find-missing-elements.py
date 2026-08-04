class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1,len(nums)):
            for j in range(nums[i-1]+1,nums[i]):
                res.append(j)
        return res
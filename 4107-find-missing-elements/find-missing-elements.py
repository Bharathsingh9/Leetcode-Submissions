class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        M = max(nums)
        N = min(nums)
        ans = []
        for i in range(N,M):
            if i not in nums:
                ans.append(i)
        return ans
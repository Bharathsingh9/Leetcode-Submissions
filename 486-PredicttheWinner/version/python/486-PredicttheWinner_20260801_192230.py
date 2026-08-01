# Last updated: 8/1/2026, 7:22:30 PM
1class Solution:
2    def predictTheWinner(self, nums: List[int]) -> bool:
3        n = len(nums)
4        if n % 2 == 0: 
5            return True 
6        dp = list(nums)
7        for i in range(n - 2, -1, -1):
8            for j in range(i + 1, n):
9                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
10        return dp[-1] >= 0
11        
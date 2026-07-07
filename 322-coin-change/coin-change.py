class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [ [float('inf')]*(amount+1) for i in range(1+len(coins)) ]

        for i in range(1+len(coins)):
            dp[i][0] = 0

        for i in range(1,1+len(coins)):
            for j in range(1,1+amount):
                if j-coins[i-1] < 0  :
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j]  = min(dp[i][j-coins[i-1]] + 1,dp[i-1][j])
        
        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]
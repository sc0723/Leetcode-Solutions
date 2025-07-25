class Solution:
    def climbStairs(self, n: int) -> int:
        ## DP Solution
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
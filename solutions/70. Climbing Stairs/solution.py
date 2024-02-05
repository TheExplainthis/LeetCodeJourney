class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (1 + n)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

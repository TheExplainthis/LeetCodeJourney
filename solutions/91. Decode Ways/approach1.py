class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            two_digit = int(s[i - 2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

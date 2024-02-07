class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return ""
        
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    count += 1
                    dp[i][j] = True

        return count

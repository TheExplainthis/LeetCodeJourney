from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i < len(word):
                    continue
                
                if i == len(word) or dp[i - len(word)]:
                    if s[i - len(word):i] == word:
                        dp[i] = True
                        break

        return dp[-1]

# i = 0 1 2 3 4 5 6 7 8 9 10 11 12 13
#       a p p l e p e n a p  p  l  e
# dp =  F F F F T F F T F F  F  F  T
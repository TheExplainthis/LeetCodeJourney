# Coin Change

[題目連結](https://leetcode.com/problems/coin-change/description/)

## 題目描述
原文：
  
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount.* If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

----

GPT 4 翻譯：

您被給定一個整數數組 `coins`，代表不同面額的硬幣，以及一個整數 `amount`，代表總金額。

返回構成該金額所需的最少硬幣數量。如果無法使用這些硬幣的任何組合來湊成該金額，則返回 `-1`。

您可以假設每種硬幣有無限個。

----

Example 1
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

Example 2
```
Input: coins = [2], amount = 3
Output: -1
```

Example 3
```
Input: coins = [1], amount = 0
Output: 0
```

Constraints:
* `1 <= coins.length <= 12`
* `1 <= coins[i] <= 2^31 - 1`
* `0 <= amount <= 10^4`


## 思路：

這題如果是暴力解的話，就是把所有組合找出來，最後把最少的硬幣數來當作答案。不用作應該都會知道這樣的做法會需要耗費很多時間，因為他是一個重複組合的題型，對應到程式碼，就是需要用 Backtracking 的方式來實作。

這題可以直接來思考動態規劃的做法，首先如果是 DP 的話，可以先思考狀態為何，這邊可能的思考是：
1. `dp[1]` 表示 1 塊錢的最少硬幣數。
2. `dp[2]` 表示 2 塊錢的最少硬幣數。
3. `dp[3]` 表示 3 塊錢的最少硬幣數。
最後返回 `dp[amount]` 應該就會是答案。

所以轉移方程式為：
```
for coin in coins:
    dp[n] = min(dp[n], dp[n - coin])
```

* 複雜度：
  * 時間複雜度：O(S * N)
  * 空間複雜度：O(S)
  * 其中 S 為 amount、N 為硬幣數

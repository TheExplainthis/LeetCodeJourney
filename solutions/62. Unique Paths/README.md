# Unique Paths

[題目連結](https://leetcode.com/problems/unique-paths/description/)

## 題目描述
原文：
  
There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner.*

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

----

GPT 4 翻譯：

有一個機器人在一個 `m x n` 的網格上。機器人最初位於**左上角**（即，`grid[0][0]`）。機器人試圖移動到**右下角**（即，`grid[m - 1][n - 1]`）。機器人在任何時候只能向下或向右移動。

給定兩個整數 `m` 和 `n`，返回機器人到達右下角的可能的唯一路徑數量。

測試案例生成的方式，使得答案將小於或等於 `2 * 10^9`。

----

Example 1
![Example 1](example1.png)
```
Input: m = 3, n = 7
Output: 28
```

Example 2
```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

Constraints:
* `1 <= m, n <= 100`


## 思路：

這題的每一個選項，可以取、或不取，所以以暴力窮舉來說，可以到 2^n 次方種，類似這種題型的題目，都可以嘗試用 DP 來解。首先思考 dp 的狀態是什麼，可能有以下幾種可能： 
1. `dp[i][j]` 表示 index 第 i 到第 j 的範圍區間最長的嚴格遞增子序列。
2. `dp[i]` 表示 index 從第 0 到第 i 的範圍區間最長的嚴格遞增子序列。

因為題目必須要從 index = 0 開始看，所以可以簡化成第二種，而轉移方程為：  
```
dp[i] = 上一個狀態 + 1 if nums[i] > 上一個狀態所在數字
```
意思是什麼呢？ 意思是，如果今天輸入為：`[1,3,2,5]`  
當 `index = 3, nums[index] = 5` 時，他要回頭去看所有狀況，包含：  
1. 和 `index = 0` 比較，如果 `nums[3] > nums[0]` 則 `dp[3] = dp[0] + 1` 為 `2`。  
2. 和 `index = 1` 比較，如果 `nums[3] > nums[1]` 則 `dp[3] = dp[1] + 1` 為 `3`。  
3. 和 `index = 2` 比較，如果 `nums[3] > nums[2]` 則 `dp[3] = dp[2] + 1` 為 `3`。  
最後 `dp[3]` 再從上面當中找出最長的可能性。所以程式碼會寫成：  

```python
for i in range(1, len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
```

* 複雜度：
  * 時間複雜度：O(N^2)
  * 空間複雜度：O(N)


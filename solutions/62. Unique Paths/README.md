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

如果還記得高中數學，這題就是經典的排列問題，以 Example 1 來說從最左上角到最右下角，需要有六個向右、兩個向下，所以總共的排列數就是 `(6 + 2)!/(6! * 2!) = 28`。

但如果對應到計算機領域，要寫程式的話，應該怎麼辦呢？如果前面題目有認真的寫的話，就會記得回溯法（Backtracking）非常適合處理排列、組合、集合的題型，不過回溯法會把所有的排列的可能性列出來，但這題不用，只需要求最後的數字，所以可以用動態規劃 （Dynamic Programming）來做。

動態規劃最難的，就是要去定義狀態，這題的狀態還很簡單，可以定義：`dp[i][j]` 表示第 (i, j) 位置的方法數，所以轉移方程可以寫成： 
```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```


* 複雜度：
  * 時間複雜度：O(N^2)
  * 空間複雜度：O(N^2)

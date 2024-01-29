# Number of Islands

[題目連結](https://leetcode.com/problems/number-of-islands/description/)

## 題目描述
原文：

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

----

GPT 4 翻譯：

給定一個 `m x n` 的二維二進制網格 `grid`，它代表了由 `'1'`（陸地）和 `'0'`（水域）構成的地圖，返回島嶼的數量。

一個**島嶼**被水域包圍，並且是通過水平或垂直相鄰的陸地相連而形成的。你可以假設網格的所有四個邊界都被水域包圍。

----

Example 1
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

```

Example 2

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Constraints:

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`.

## 思路

這題很適合使用 DFS，因為可以針對鄰近的 1 做深度搜尋，搜尋到的陸地會全部轉成 0 ，以確保他下次不會在被計算到。

**方法: DFS**
* 步驟
  * **遍歷網格**：從左上角開始，遍歷整個網格。對於每個單元格，如果它是 '1'（陸地），則進行進一步的探索。
  * **深度優先搜索（DFS）**：
    * 當找到一塊陸地時，使用深度優先搜索來探索與之相鄰的所有陸地單元格。這包括水平或垂直方向的相鄰單元格。
    * 在探索過程中，將訪問過的陸地單元格標記為 '0' 或其他標記，以避免重複計算。
  * **計數島嶼**：
    * 每當從一個未探索的 '1'（陸地）開始一次新的 DFS 探索時，島嶼數量加一。
    * DFS 保證了所有與當前陸地單元格相連的陸地都會被探索，因此每次進行 DFS 都代表發現了一個新島嶼。
  * **返回結果**：經過整個網格的遍歷後，返回計數的島嶼數量。

* 複雜度
  * 時間複雜度: O(M * N)
  * 空間複雜度: O(M * N)
    * 若使用 BFS 則為：O(min(M, N))

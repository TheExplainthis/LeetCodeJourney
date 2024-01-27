# Word Search

[題目連結](https://leetcode.com/problems/word-search/description/)

## 題目描述
原文：

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if `word` exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


----

GPT 4 翻譯：

給定一個 `m x n` 的字符網格 `board` 和一個字符串 `word`，如果 `word` 在網格中存在，則返回 `true`。

單詞可以由順序相鄰單元格的字母構成，其中相鄰單元格是水平或垂直鄰接的。同一個字母單元格不能被使用超過一次。

----

Example 1

![Example 1](example1.jpeg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

Example 2

![Example 2](example2.jpeg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

Example 3

![Example 3](example3.jpeg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

Constraints:

* `m == board.length`
* `n = board[i].length`
* `1 <= m, n <= 6`
* `1 <= word.length <= 15`
* `board` and `word` consists of only lowercase and uppercase English letters.


## 思路

這題和 [200. Number of Islands](https://leetcode.com/problems/number-of-islands) 很像，就是用 DFS 不斷地往外擴，去找相對應的字母，而要注意的事情在於走過的路不得重複走，以及如果已經沒有對應的字母了，就可先停止（剪枝）不用再繼續往下找。所以這樣的做法，更精確來說是 Backtracking 的做法。


**方法: Backtracking**

* 步驟
  1. 遍歷網格：從網格的每一個單元格開始尋找。遍歷整個網格，對每個單元格執行後續的搜索步驟。
  2. 回溯搜索：當你在網格中選擇一個單元格作為起點時，基於這個單元格，使用回溯法尋找是否能構成目標單詞。
  3. 檢查相鄰單元格：從選定的單元格開始，檢查所有水平或垂直相鄰的單元格，看它們是否包含單詞的下一個字母。
  4. 標記和回溯：在遍歷過程中，暫時標記已經訪問過的單元格，以避免重複使用。完成對一個單元格的探索後，取消標記，以便進行後續的搜索。
  5. 檢查完成條件：如果某一路徑上的字母順序與單詞匹配，則返回真（true）；否則繼續尋找其他路徑。
  6. 返回結果：如果在網格中找到了匹配的單詞，則返回真（true），否則返回假（false）。

* 複雜度
  * 時間複雜度: O(N * 4^L)，其中 N 是網格中的單元格數量（m x n），L 是單詞的長度。最壞情況下，需要對每個單元格進行深度為 L 的搜索。
  * 空間複雜度: O(L)，主要是由於遞歸堆棧的深度，在最壞情況下會達到單詞的長度 L。

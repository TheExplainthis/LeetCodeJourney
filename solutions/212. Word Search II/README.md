# Word Search II

[題目連結](https://leetcode.com/problems/word-search-ii/description/)

## 題目描述
原文：

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board.*

Each word must be constructed from letters of sequentially **adjacent cells**, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

----

GPT 4 翻譯：

給定一個 `m x n` 的字符版 `board` 和一個字符串列表 `words`，返回 *版上的所有單詞*。

每個單詞必須由連續 **相鄰單元格** 的字母構成，其中相鄰單元格是水平或垂直鄰近的。在一個單詞中，同一個字母單元格不得使用超過一次。


----

Example 1:
![Example 1](example1.jpeg)
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

Example 2:
![Example 2](example2.jpeg)
```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

Constraints:

* `m == board.length`
* `n == board[i].length`
* `1 <= m, n <= 12`
* `board[i][j]` is a lowercase English letter.
* `1 <= words.length <= 3 * 10^4`
* `1 <= words[i].length <= 10`
* `words[i]` consists of lowercase English letters.
* All the strings of `words` are unique.

## 思路

這題和 [200. Number of Islands](https://leetcode.com/problems/number-of-islands) 很像，會覺得用一個 DFS 去展開，每一步往外為擴時，就去對應看看是否有出現對應的字母。 

整個思維是正確的，但有幾個可以調整的地方：  
1. 同一個單詞中，走過的路不得再走
2. 如果每一個單詞都要針對整個二維陣列做一次 DFS ，就會變成是 O(長 * 寬 * 單詞數量 * 單詞長度) = O( M * N * Word * 4^Length)，這樣可能會 TLE。
  
要調整的做法為：  
1. 建立一個 Trie ，讓這些單詞可以重新用 Trie 的形式來做建構。 O(Word * Length)
2. 再利用 Backtracking 來判斷路徑組成的單詞是否為在 Trie 中，若前綴就發現不吻合，就直接跳出，避免無效的運算。 O( M * N * 4^Length)

**方法: Trie + Backtracking**

* 步驟
  1. 建立 Trie：遍歷所有單詞，將它們加入 Trie。這樣可以快速檢查字母序列是否與任何單詞的前綴匹配。
  2. 初始化 Backtracking：
    * 對字母板的每個單元格進行遍歷，對每個單元格啟動一次 Backtracking 搜索。
  3. Backtracking 搜索：
    * 從當前單元格開始，探索所有可能的路徑。如果當前路徑在 Trie 中匹配到單詞的前綴，則繼續搜索；否則，回溯。
  4. 記錄找到的單詞：
    * 每當在 Trie 中找到一個完整的單詞時，將其記錄下來。
  5. 避免重複使用單元格：
    * 在搜索過程中，標記當前路徑使用過的單元格，並在回溯時將其恢復。

* 複雜度
    * 時間複雜度:O(W × L + M × N × 4^L)
      * W 是單詞數量，L 是單詞的平均長度，用於建立 Trie 的時間。
      * M × N 是字母板的尺寸，每個單元格啟動一次最多到深度 L 的 Backtracking 搜索。
    * 空間複雜度: O(W × L)

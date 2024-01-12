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

![Example 1](example1.png)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

Example 2

![Example 2](example2.png)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

Example 3

![Example 3](example3.png)

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

這題主要在考的是寫程式的能力，因為這題很直觀，每一個格子要比三次：橫列、直行、九宮格，總共為 N*N 格（此時 N 為 9），所以時間複雜度至少為 O(N^2)，需要考量以下幾個點：
1. 比對該列、該行或該九宮格是否為 1-9 時，需要耗費多少時間？
2. 感覺一直在比對一樣的東西、但方向上有點不同，該怎麼寫出好程式碼？


**方法 1: 利用 Set**

* 步驟
    1. 初始化：
        ```python
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        ```

    2. 掃過整格 9 * 9 的格子，邊掃的時候，邊放入三個地方：該列、該行、該九宮格，如下：
        ```python
        for r in range(N):
            for c in range(N):
                ...
                rows[r].add(number)
                cols[c].add(number)

                idx = (r // 3) * 3 + c // 3
                boxes[idx].add(number)
                ...
        ```
        一但發現重複就 return False

* 複雜度
    * 時間複雜度: O(N^2)   
    * 空間複雜度: O(N^2)
    * 備註：因為 N 一定是常數 9 ，所以也可視為 O(1)

* 備註
    * 開一個長度為 9 的陣列也可以達到一樣的效果。

**方法 2: Bitmask**

為了讓空間複雜度更低，提供了另一種思路，是將每一格的數字，當作是二進位 9 bits 的每一格，舉例來說：
```
5 3 .      數字：    9 8   6 5   3 
6 . .  =>  對應位置： 1 1 0 1 1 0 1 0 0
. 9 8
```
用這樣的方式儲存，可以達到同樣的效果，判斷是否重複只要判斷該對應位置是否為 1 就可以知道 (val & 對應位置的值)

* 步驟
    1. 初始化：
        ```python
        N = 9
        rows = [0]
        cols = [0]
        boxes = [0]
        ```
    2. 掃過整格 9 * 9 的格子，邊掃的時候，邊放入三個地方：該列、該行、該九宮格，如下：
        ```python
        for r in range(N):
            for c in range(N):
                ...
                bit_flag = int(board[r][c]) - 1

                rows[r] |= (1 << bit_flag)
                cols[c] |= (1 << bit_flag)

                idx = (r // 3) * 3 + c // 3
                boxes[idx] |= (1 << bit_flag)
                ...
        ```
        一但發現重複就 `return False`

* 複雜度
    * 時間複雜度: O(N^2)
    * 空間複雜度: O(N)
    * 備註：因為 N 一定是常數 9 ，所以也可視為 O(1)


## 本題學習

1. 若要比對是否存在的數字 1 ~ N：
* 長度 N 固定
    * 長度超出 int 範圍：可以用陣列
    * 長度不超出 int 範圍：可以用 Bitmask
* 長度 N 不固定
    * 只能用 Set 來處理。
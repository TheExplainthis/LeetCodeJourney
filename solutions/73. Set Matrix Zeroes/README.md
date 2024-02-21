# Set Matrix Zeroes

[題目連結](https://leetcode.com/problems/set-matrix-zeroes/description/)

## 題目描述
原文：
  
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.


----

GPT 4 翻譯：

給定一個 `m x n` 整數矩陣 `matrix`，如果一個元素為 `0`，則將其所在的整行和整列設為 `0`。

你必須就地完成此操作。

----

Example 1  
![example1](./example1.jpeg)  
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

Example 2  
![example2](./example2.jpeg)  
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

Constraints:
* `m == matrix.length`
* `n == matrix[0].length`
* `1 <= m, n <= 200`
* `-2^31 <= matrix[i][j] <= 2^31 - 1`

## 思路：

這題看似需要用 DFS 去更新 0 所在的橫軸與縱軸的值，但因為每一次都直接更新陣列上的數值，所以無法分辨哪些是原本的 0 ，哪些是被更新的 0，以至於有可能有一格為 0 的話，導致全部都被設為 0 。

簡單的做法為，我先掃過每一格，如果 `matrix[i][j]` 為 0 的話，那我就先把 `matrix[i][0]` 和 `matrix[0][j]` 設為 0，全部做完後，我就可以知道哪些欄、哪些列要設為 0 了。

注意：第一行與第一列被當作狀態管理使用，所以如果原本陣列第一行第一列有 0 出現的話，要再分開處理。

* 複雜度：
  * 時間複雜度：O(m * n)
  * 空間複雜度：O(1)

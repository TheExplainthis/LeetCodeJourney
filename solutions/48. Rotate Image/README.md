# Rotate Image

[題目連結](https://leetcode.com/problems/rotate-image/description/)

## 題目描述
原文：
  
You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

----

GPT 4 翻譯：

你被給予一個 `n x n` 的二維 `matrix`，代表一張圖像，將圖像順時針旋轉 **90** 度。

你必須就地旋轉圖像，這意味著你必須直接修改輸入的二維矩陣。**不要** 分配另一個二維矩陣來進行旋轉。

----

Example 1  
![example1](./example1.jpeg)  
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

Example 2  
![example2](./example2.jpeg)  
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

Constraints:
* `n == matrix.length == matrix[i].length`
* `1 <= n <= 20`
* `-1000 <= matrix[i][j] <= 1000`

## 思路：

這是一道 simulation 的題型，意指他要你做什麼，你就怎麼做，就可以順利做完，通常會考驗你的想像力、觀察力、或者是寫程式的能力，以這題為例，你可以在 Dry Run 的時候找出一個規律，了解他旋轉的方式。

也可以透過觀察題目發現，如過是順時針轉 90 度，那就代表先從對角翻轉，在左右翻轉，就可以完成正時針旋轉 90 度，這樣的方式程式碼簡潔又好懂。

* 複雜度：
  * 時間複雜度：O(N^2)
  * 空間複雜度：O(1)
  * 其中 N 為邊長

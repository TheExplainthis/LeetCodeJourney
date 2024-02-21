# Spiral Matrix

[題目連結](https://leetcode.com/problems/spiral-matrix/description/)

## 題目描述
原文：
  
Given an `m x n` `matrix`, return *all elements of the `matrix` in spiral order.*

----

GPT 4 翻譯：

給定一個 `m x n` 的 `matrix`，返回 *`matrix` 中所有元素的螺旋順序。*

----

Example 1  
![example1](./example1.jpeg)  
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Example 2  
![example2](./example2.jpeg)  
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

Constraints:
* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`

## 思路：

這題和 48 題一樣，照著題目的敘述去完成即可。

* 複雜度：
  * 時間複雜度：O(m * n)
  * 空間複雜度：O(1)

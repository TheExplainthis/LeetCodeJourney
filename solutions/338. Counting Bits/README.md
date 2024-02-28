# Counting Bits

[題目連結](https://leetcode.com/problems/counting-bits/description/)

## 題目描述
原文：
  
Given an integer `n`, return an array ans of length `n + 1` such that for each i (`0 <= i <= n`), `ans[i]` is the **number of `1`'s** in the binary representation of `i`.

----

GPT 4 翻譯：

給定一個整數 `n`，返回一個長度為 `n + 1` 的數組 `ans`，使得對於每個i（`0 <= i <= n`），`ans[i]` 是 `i` 的二進制表示中**`1`的數目**。

----

Example 1
```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

Example 2
```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

Constraints:
* `0 <= n <= 10^5`


## 思路：

看到 bit 的題型，建議可以先將整數列成二位元，然後再來觀察規律：

```
整數 -> 位元數, 1 的個數
0 --> 0      0
1 --> 1      1
2 --> 10     1
3 --> 11     2
4 --> 100    1
5 --> 101    2
6 --> 110    2
7 --> 111    3
8 --> 1000   1
9 --> 1001   2
10 -> 1010   2
11 -> 1011   3
12 -> 1100   2
13 -> 1101   3
14 -> 1110   3
15 -> 1111   4
```

觀察出什麼規律了呢？可以思考的事情是， 數字 5 所佔的 1 個數和數字 4 所佔的 1 個數關聯是什麼？如下圖所示：

[!image1](./image1.png)

任何整數 `X` 和 `X - 1` 的前半段，一定會有一樣的 1 個數，只要兩個做 `&` 就可以把共同的地方找出來，

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)

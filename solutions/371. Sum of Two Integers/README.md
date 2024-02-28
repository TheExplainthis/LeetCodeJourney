# Sum of Two Integers

[題目連結](https://leetcode.com/problems/sum-of-two-integers/description/)

## 題目描述
原文：
  
Given two integers `a` and `b`, return *the sum of the two integers without using the operators `+` and `-`.*
 
----

GPT 4 翻譯：

給定兩個整數 `a` 和 `b`，返回*兩個整數的和，而不使用運算符 `+` 和 `-`。*

----

Example 1
```
Input: a = 1, b = 2
Output: 3
```

Example 2
```
Input: a = 2, b = 3
Output: 5
```

Constraints:
* `-1000 <= a, b <= 1000`


## 思路：

不能用加法完成加法的動作，就可以回到位元的運算來看，可以參考下圖：  
[!image](./image.png)

可以得到一個加法運作是：
```
C = A ^ B
Carry = A & B
```

這樣做會有 2 個問題：
1. C 和 Carry 在過程中很有可能會溢位，超出 32 位元，所以要用一個 mask 來處理。
2. 如果數字大於 0x7FFFFFFF 代表是負數，因為開頭為 1 表示負號，所以如果是負的話，就要回傳他的 1 補數。

* 複雜度：
  * 時間複雜度：O(1)
  * 空間複雜度：O(1)

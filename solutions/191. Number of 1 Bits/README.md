# Number of 1 Bits

[題目連結](https://leetcode.com/problems/number-of-1-bits/description/)

## 題目描述
原文：
  
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

**Note:**

* Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in **Example 3**, the input represents the signed integer. `-3`.

----

GPT 4 翻譯：

撰寫一個函式，接受一個無符號整數的二進制表示，並返回它擁有的'1'位的數目（也被稱為[漢明重量](http://en.wikipedia.org/wiki/Hamming_weight)）。

**注意：**

* 注意，在一些語言中，如Java，沒有無符號整數類型。在這種情況下，輸入將作為有符號整數類型給出。這不應該影響你的實現，因為無論是有符號還是無符號，整數的內部二進制表示是相同的。
* 在Java中，編譯器使用2的補數表示法來表示有符號整數。因此，在**示例3**中，輸入代表有符號整數 `-3`。

----

Example 1
```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

Example 2
```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```

Example 3
```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

Constraints:
* The input must be a **binary string** of length `32`.


## 思路：

bit 的題型，會需要先看清楚輸入，有時候會給整數，有時候會給字串。而若題目給的是整數，則可以直接操作，程式語言在操作二位元時，如果遇到 `&`、`|`、`>>`、`<<` 等位元操作符號時，就可以用位元的方式來看待這個整數，意思是：

```
print(1 << 1)  # 輸出：2，因為 1 往右移一格，位元變成 10，得到整數 2
print(5 & 4)   # 輸出：4，因為 101 & 100，位元變成 100，得到整數 4
```

而以這題簡單的做法，就是用一個 mask 掃過整個位元，如果 `&` 得到 1，代表該為元是 1，最後統計起來即可。

```
count = 0
mask = 1
for i in range(32):
    if n & mask != 0:
        count += 1
    mask << 1
return count
```

* 複雜度：
  * 時間複雜度：O(32) = O(1)
  * 空間複雜度：O(1)

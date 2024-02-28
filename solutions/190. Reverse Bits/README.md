# Number of 1 Bits

[題目連結](https://leetcode.com/problems/number-of-1-bits/description/)

## 題目描述
原文：
  
Reverse bits of a given 32 bits unsigned integer.

**Note:**

* Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in **Example 2** above, the input represents the signed integer `-3` and the output represents the signed integer `-1073741825`.
 
----

GPT 4 翻譯：

反轉一個給定的32位無符號整數的位元。

**注意：**

* 注意，在某些語言中，如Java，沒有無符號整數類型。在這種情況下，輸入和輸出都將作為有符號整數類型給出。它們不應該影響你的實現，因為不論是有符號還是無符號，整數的內部二進制表示是相同的。
* 在Java中，編譯器使用2的補數表示法來表示有符號整數。因此，在上面的**示例 2**中，輸入代表有符號整數`-3`，輸出代表有符號整數`-1073741825`。

----

Example 1
```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

Example 2
```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

Constraints:
* The input must be a **binary string** of length `32`.


## 思路：

可以直接照著題目的要求操作，將最右邊的位元優先加總到結果中，從右做到左做完後，答案就得到了。

```python
result = 0
power = 31    # 從最左邊的位元開始

while n:
    result += (n & 1) << power  # 如果是 1 就往位移 power 位
    n = n >> 1 # 刪除最右邊的位元
    power -= 1

return result        
```


* 複雜度：
  * 時間複雜度：O(32) = O(1)
  * 空間複雜度：O(1)

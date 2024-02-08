# Maximum Product Subarray

[題目連結](https://leetcode.com/problems/maximum-product-subarray/description/)

## 題目描述
原文：
  
Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

----

GPT 4 翻譯：

給定一個整數數組 `nums`，找到一個具有最大乘積的子數組，並返回*該乘積*。

測試案例生成的方式，使得答案將適合於一個 **32 位**整數。

----

Example 1
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

Example 2
```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```


Constraints:
* `1 <= nums.length <= 2 * 10^4`
* `-10 <= nums[i] <= 10`
* The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.


## 思路：

在思考這題時，可以看一下題目限制，他要求是 subarray，subarray 是要連續的，不能隨意亂取，所以這題應該是要回傳從 `nums` 第 `i` 個乘到第 `j` 個，可以得到最大值。也就是說某一個範圍乘起來會得到最大。

這題會衍生出幾種思考的做法：
1. 利用 Sliding Window：盡可能的找出最大的窗口做相乘。
2. 利用動態規劃 DP： 找出 `dp[i][j] = ?` 的轉移方程式。
  
方法 1：Sliding Window
不太可行，因為用快慢指針時，找不到快慢指針的移動依據，例如：  
`nums = [1, -1, 2, 3]`，可能有人會誤以為，當整體相乘為總值 < 0 時，快指針停下來，慢指針就可以往前走，走到 > 0 的時候，但是別忘了，數學有負負得正，所以快指針很有可能再往後走很有可能碰到負號，就會變成最大值了。  

方法 2：Dynamic Programming
除了一開始說的要找出 `dp[i][j] = ?` 的這種狀態表示法以外，還有另外一種 DP 的形式，就是來記錄狀態的，這種題型常出現在股票買賣的考題當中，他主要會利用 DP 來記錄狀態，以這題來看：  
 
**核心邏輯為：就算當下乘到數字後得到負數，但後面有機會負負得正，因此不得拋棄他。**
  
`nums = [2, 3, -2, 4, -1, 3]` 可以用兩個 DP 來紀錄，一個是最大值，一個是最小值。  
我們先來看成果： 
`max_dp = [2, 6, -2, 4, 48, 144]`  
`min_dp = [2, 3, -12, -48, -4, -12]`  

再來看看每一個數字怎麼出來的？  
1. max_dp[0] = max_dp[0] = 初始化 nums[0]
2. max_dp 會有幾個選項：
   1. 如果 nums[i] < 0：那就可以看看 min_dp 的數字抓過來看看能不能負負得正；不能的話就拋棄一切，從 nums[i] 開始累積。
   2. 如果 nums[i] > 0：那就繼續往下乘就對了。

所以 max_dp 為：  
```python
if nums[i] < 0:
    max_dp[i] = max(min_dp[i - 1] * nums[i], nums[i])
else:
    max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i])
```

反過來 min_dp 為：  
```python
if nums[i] < 0:
    min_dp[i] = min(max_dp[i - 1] * nums[i], nums[i])
else:
    min_dp[i] = min(min_dp[i - 1] * nums[i], nums[i])
```

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)

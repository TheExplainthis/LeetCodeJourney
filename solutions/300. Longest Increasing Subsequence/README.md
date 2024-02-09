# Longest Increasing Subsequence

[題目連結](https://leetcode.com/problems/longest-increasing-subsequence/description/)

## 題目描述
原文：
  
Given an integer array `nums`, return the length of the longest **strictly increasing** subsequence.

----

GPT 4 翻譯：

給定一個整數數組 `nums`，返回最長**嚴格遞增**子序列的長度。

----

Example 1
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

Example 2
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

Example 3
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

Constraints:
* `1 <= nums.length <= 2500`
* `-10^4 <= nums[i] <= 10^4`


## 思路：

這題的每一個選項，可以取、或不取，所以以暴力窮舉來說，可以到 2^n 次方種，類似這種題型的題目，都可以嘗試用 DP 來解。首先思考 dp 的狀態是什麼，可能有以下幾種可能： 
1. `dp[i][j]` 表示 index 第 i 到第 j 的範圍區間最長的嚴格遞增子序列。
2. `dp[i]` 表示 index 從第 0 到第 i 的範圍區間最長的嚴格遞增子序列。

因為題目必須要從 index = 0 開始看，所以可以簡化成第二種，而轉移方程為：  
```
dp[i] = 上一個狀態 + 1 if nums[i] > 上一個狀態所在數字
```
意思是什麼呢？ 意思是，如果今天輸入為：`[1,3,2,5]`  
當 `index = 3, nums[index] = 5` 時，他要回頭去看所有狀況，包含：  
1. 和 `index = 0` 比較，如果 `nums[3] > nums[0]` 則 `dp[3] = dp[0] + 1` 為 `2`。  
2. 和 `index = 1` 比較，如果 `nums[3] > nums[1]` 則 `dp[3] = dp[1] + 1` 為 `3`。  
3. 和 `index = 2` 比較，如果 `nums[3] > nums[2]` 則 `dp[3] = dp[2] + 1` 為 `3`。  
最後 `dp[3]` 再從上面當中找出最長的可能性。所以程式碼會寫成：  

```python
for i in range(1, len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
```

* 複雜度：
  * 時間複雜度：O(N^2)
  * 空間複雜度：O(N)

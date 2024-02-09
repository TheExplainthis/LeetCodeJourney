# Longest Common Subsequence

[題目連結](https://leetcode.com/problems/longest-common-subsequence/description/)

## 題目描述
原文：
  
Given two strings `text1` and `text2`, return *the length of their longest **common subsequence***. If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`.
A **common subsequence** of two strings is a subsequence that is common to both strings.

----

GPT 4 翻譯：

給定兩個字符串 `text1` 和 `text2`，返回*它們最長的**共同子序列**的長度*。如果沒有**共同子序列**，則返回 `0`。

一個字符串的**子序列**是從原始字符串生成的新字符串，其中一些字符（可以沒有）被刪除，但不改變剩餘字符的相對順序。

例如，`"ace"` 是 `"abcde"` 的一個子序列。
兩個字符串的**共同子序列**是兩個字符串都有的子序列。


----

Example 1
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

Example 2
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

Example 3
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

Constraints:
* `1 <= text1.length, text2.length <= 1000`
* `text1` and `text2` consist of only lowercase English characters.


## 思路：

同樣是字符比對 DP 的題型，可以比較看看 [5. Longest Palindromic Substring](../5.%20Longest%20Palindromic%20Substring/)，先來看看他的轉移方程式：  

**5. Longest Palindromic Substring**
```
dp[i][j] = dp[i + 1][j - 1] # if nums[i] == nums[j]
```

通常字串比對相關的題目，都會需要利用一個二維陣列來處理，而回文就是自己跟自己比較，所以需要二維陣列，而這題就是兩個字串做比較。而這題可以先定義狀態，一個變數 `i` 指向 `text1`、一個變數 `j` 指向 `text2`。所以 `dp[i][j]` 表示 `text1` 指向第 i 個位置與 `text2` 指向第 j 個位置的最長共同子序列。

轉移方程式為：
```
dp[i][j] = dp[i-1][j-1] + 1 # if text1[i] == text2[j]
dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 前者表示 text1 的第 i 個不選、後者表示 text2 的第 j 個不選。
```

dp 最後可以得到以下的陣列。
```
   i = a b c d e
j=
a      1 1 1 1 1
c      1 1 2 2 2
e      1 1 2 2 3
```

* 複雜度：
  * 時間複雜度：O(M * N)
  * 空間複雜度：O(M * N)
  * M 和 N 分別表示 `text1` 以及 `text2` 的長度。

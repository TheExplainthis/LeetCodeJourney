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

這題看似要用 Backtracking 把所有的解法找出來，再計算總和，但其實大可不必，因為 Dynamic Programming 特別擅長使用在這種情境。

## 方法 A: Dynamic Programming

此時要先找到動態規劃的狀態為何？以回文的題目來看，狀態可以設定為，雖然 `s[i] == s[j]`，但是 `字串 i ~ j` 是不是回文，那就得看 `字串 i + 1 ~ j - 1` 是不是回文。就可以不斷地遞迴下去找。所以：  
```python
dp[i][j] = dp[i + 1][j - 1] # if s[i] == s[j]
```

這時候可以得到一個二維的陣列，這題只要把陣列上所有為 True 的格子加總，就可以得到答案了。

* 複雜度：
  * 時間複雜度：O(N^2)
  * 空間複雜度：O(N^2)

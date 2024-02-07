# Palindromic Substrings

[題目連結](https://leetcode.com/problems/palindromic-substrings/description/)

## 題目描述
原文：
  
Given a string `s`, return *the number of **palindromic substrings** in it.*

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

----

GPT 4 翻譯：

給定一個字符串 `s`，返回*其中**回文子串**的數量*。

當一個字符串從後向前讀和從前向後讀相同時，它就是一個**回文串**。

**子串**是字符串內連續的字符序列。

----

Example 1
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

Example 2
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

Constraints:
* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.


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

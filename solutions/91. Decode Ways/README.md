# Decode Ways

[題目連結](https://leetcode.com/problems/decode-ways/description/)

## 題目描述
原文：
  
A message containing letters from `A-Z` can be **encoded** into numbers using the following mapping:
```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```
To **decode** an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

* `"AAJF"` with the grouping `(1 1 10 6)`
* `"KJF"` with the grouping `(11 10 6)`
Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return *the *number* of ways to *decode* it.*

The test cases are generated so that the answer fits in a **32-bit** integer.

 

----

GPT 4 翻譯：

一條包含從 `A-Z` 的字母的訊息可以使用以下映射被**編碼**成數字：

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

為了**解碼**一條已編碼的訊息，所有的數字必須被分組然後使用上述映射的反向映射回字母（可能有多種方式）。例如，`"11106"`可以被映射成：

* `"AAJF"` 透過分組 `(1 1 10 6)`。
* `"KJF"` 透過分組 `(11 10 6)`。

注意分組 `(1 11 06)` 是無效的，因為 `"06"` 不能被映射成 `'F'`，由於 `"6"` 和 `"06"` 不同。

給定一個只包含數字的字符串 `s`，*返回**解碼**它的方法數*。

測試案例生成的方式是使答案適合於一個 **32位** 整數。

----

Example 1
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

Example 2
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

Example 3

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

Constraints:
* `1 <= s.length <= 100`
* `s` contains only digits and may contain leading zero(s).


## 思路：

這題看似要用 Backtracking 把所有的解法找出來，再計算總和，但其實大可不必，因為 Dynamic Programming 特別擅長使用在這種情境。

## 方法 A: Dynamic Programming

在找 DP 的轉移方程式時，可以先直接把 dp 的每一個欄位要放的東西，先假設跟題目要求的輸出結果是相同的，例如：`dp[0]` 表示字符長度為 0 時的方法數；`dp[1]` 表示字符長度為 1 時的方法數，所以要求 `dp[len(s)]` 為何？

先這樣想了之後，方法就會簡單很多，你可以慢慢推導看看，並嘗試找到規律。  

**先看到字串為 1 時：包含的可能性有 -> `0`、`3`**
* `0` -> 因爲題目有說 `01` 和 `1` 是不同的，所以這個 `0` 一定是屬於前面其他數字的，因此看到 `0` 的時候代表方法數不會增加。
* `3` -> 看到一個位數 `1` ~ `9` 一定存在一個作法是解碼成 `a` ~ `i`，但方法數不會變多。


**當字符串為 2 時：包含的可能性有 -> `10`、`13`、`27`**  
而這些方法當中，有幾種可能性？  
* `10` -> 如同字串長度為 1 時所說，看到 `0` 時，按兵不動，因為這個 `0` 是前面 `1` 的個位數，所以他只能是一種做法，就是 `(xxxx, 10)`
* `13` -> 看到 `3` 的時候，他可能有兩種可能
  * 第一種：`(xxx, 3)`， 為 `dp[i] = dp[i - 1]` 方法數維持前者
  * 第二種：`(xxx, 13)`， 為 `dp[i] = dp[i - 1] + dp[i - 2]` 方法數維持前者 + 前前者。
* `27` -> 只有一種可能，就是 `(xxx, 7)`，因為 `27` 湊成雙位數 `> 26` 了。

整理一下：  
1. 先給一個長度為 (n + 1) 的陣列長度 dp。
2. 若第 i 位字符串不為 `0` 那麼 `dp[i] = dp[i - 1]`
3. 若第 i-1 位 + 第 i 位組成雙位數介於 `10 ~ 26` 之間，那麼 `dp[i] = dp[i - 1] + dp[i - 2]`


複雜度：
- 時間複雜度：O(N)
- 空間複雜度：O(N)

## 方法 B: DP 優化版

因為上一個版本只用到兩個狀態，所以僅需要用兩個變數去記住狀態即可，詳細做法可見程式碼。

複雜度：
- 時間複雜度：O(N)
- 空間複雜度：O(1)

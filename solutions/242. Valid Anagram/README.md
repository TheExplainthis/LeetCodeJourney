# 242. Valid Anagram
[題目連結](https://leetcode.com/problems/valid-anagram/)

## 題目描述
原文：

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

----

GPT 4 翻譯：

給定兩個字符串 s 和 t，如果 t 是 s 的 Anagram，則返回 true，否則返回 false。

Anagram 是通過重新排列不同單詞或短語的字母形成的單詞或短語，通常恰好使用所有原始字母一次。

----

Example 1
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2
```
Input: s = "rat", t = "car"
Output: false
```


Constraints:

* `1 <= s.length, t.length <= 5 * 10^4`
* `s` and `t` consist of lowercase English letters.

## 思路

首先，可以估算一下這題的時間複雜度，兩個字串應該都要掃過一次，才能夠知道是否是 Anagram，因此至少需要 O(n)，接下來可以觀察一下 Anagram 的意思，會讓我們更專注於字母出現的次數，而非順序，因此可以利用空間換取時間；但如果不能用空間的話呢？是否有辦法透過排序來處理呢？因此可以衍伸出以下兩種做法：

**方法 1：排序比較法**

* 步驟
    1. 排序：將兩個字符串 s 和 t 分別進行排序。
    2. 比較：比較排序後的兩個字符串是否完全相等。

* 複雜度
    * 時間複雜度：O(NlogN)，排序通常需要 O(NlogN) 的時間。
    * 空間複雜度：O(1)，如果忽略排序時所需的額外空間。


**方法 2：使用記憶區（計數法）**

* 步驟
    1. 計數：遍歷字符串 s，記錄每個字母的出現次數。
    2. 校驗：遍歷字符串 t，減少「記憶區」中相應字母的計數，並檢查是否有不匹配的情況。

* 記憶區選擇：
    * Array：只限於小寫字母，長度為 26。
    * Counter：Python 的 Counter 結構，方便但比較時需要 O(N)。
    * Hashmap：最直觀且擴充性強。

* 複雜度
    * 時間複雜度：O(N)，僅需遍歷一次兩個字符串。
    * 空間複雜度：O(1)，字母數量有限（最多 26 個字母），視為常數級別。


## Follow Up: 非僅限小寫字母的情況

如果輸入包含不僅限於小寫字母的字符，我們需要如何調整？

* 主要影響：在這種情況下，不能單純使用固定長度的 Array 作為記憶區，因為字符種類變多。
* 解決方案：必須使用 Hashmap 或 Counter 來進行計數，以應對字符種類的增多。
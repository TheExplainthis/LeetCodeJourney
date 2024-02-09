# Word Break

[題目連結](https://leetcode.com/problems/word-break/description/)

## 題目描述
原文：
  
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

----

GPT 4 翻譯：

給定一個字符串 `s` 和一個字符串字典 `wordDict`，如果s可以被分割成一個或多個字典中的單詞的空格分隔序列，則返回 `true`。

**注意**，字典中的相同單詞在分割過程中可以被多次重用。

----

Example 1
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

Example 3

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```


Constraints:
* `1 <= s.length <= 300`
* `1 <= wordDict.length <= 1000`
* `1 <= wordDict[i].length <= 20`
* `s` and `wordDict[i]` consist of only lowercase English letters.
* All the strings of `wordDict` are **unique**.


## 思路：

這題看起來是 [322. Coin Change](../322.%20Coin%20Change/) 的變化版，利用重複組合的方式組出 `amount` 總數，而這題就是把 `wordDict` 中的每一個字做重複組合。

322 題當中，轉移方程式為：

```
for coin in coins:
    dp[i] = max(dp[i], dp[i - coin] + 1)
```

而在這題當中，轉移方程式為：
```
for word in wordDict:
    if s[i - len(word): i] == word:
        dp[i] = True
        break
```
表示如果有比對到相同的字，那就設定 dp 為 `True`，然後就不用在往其他文字做比對了，所以 Break




* 複雜度：
  * 時間複雜度：O(n * m * k)
  * 空間複雜度：O(n)
  * 其中：`n` 為 `s` 的長度，`m` 為 `wordDict` 長度，`k` 為每一個 word 平均長度。

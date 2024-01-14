# Alien Dictionary

[題目連結](https://leetcode.com/problems/alien-dictionary/description/)

## 題目描述
原文：

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `""`.

Otherwise, return *a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules. If there are multiple solutions, return **any of them.***

 

----

GPT 4 翻譯：

有一種新的外星語言，它使用英文字母表。然而，字母的順序對你來說是未知的。

你得到了一個來自這種外星語言字典的字符串列表 `words`。現在有人聲稱，`words` 中的字符串是按照這種新語言的規則按字典順序排序的。

如果這種說法是不正確的，且 `words` 中給定的字符串排列不能對應於任何字母的順序，則返回 `""`。

否則，返回按照新語言規則**字典遞增順序**排序的新外星語言中獨特字母的字符串。如果有多種解決方案，返回其中**任何一種**。

----

Example 1

```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

Example 2

```
Input: words = ["z","x"]
Output: "zx"
```

Example 3
```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

Constraints:

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 100`
* `words[i]` consists of only lowercase English letters.


## 思路

這題實作起來有點困難，但邏輯不難，用演算法的方法來看的時候，需要保持一個清晰的腦袋，因為他有兩層回圈需要做：  
Input: words = ["wrt","wrf","er","ett","rftt"]  
以這個範例來看，我們需要做以下操作：  
`word1 = wrt, word2 = wrf`，因為前兩個字母都一樣，所以 `t` 在 `f` 前面。  
`word1 = wrf, word2 = er`，第一個字母就不同，所以 `w` 在 `e` 前面。  
`word1 = er, word2 = ett`，第一個字母相同，比第二個字母，所以 `r` 在 `t` 前面。  
`word1 = ett, word2 = rftt`，第一個字母就不同，所以 `e` 在 `r` 前面。  

每一次兩個字母兩個字母比較，就可以知道哪個字母在哪一個字母前面，但是這些字母的順序性要如何重新建立呢？  
可以先利用 Graph 把關係建立起來，而因為他不未必有唯一解，因為只要和順序就好，所以剛好可以用 Topological Sort 來做。


**方法: Topological Sort**

* 步驟
  1. 建立圖：對於給定的單詞列表，我們比較相鄰單詞的每對字母，以找出字母之間的先後關係。
  2. 拓樸排序：使用深度優先搜索(DFS)來執行拓樸排序，找出正確的字母順序。
  3. 檢查是否有效：如果我們在進行拓樸排序時遇到了循環，這意味著給定的單詞列表不能對應於任何字母順序，因此返回空字串。
  4. 返回結果：如果沒有循環，則返回排序後的字母序列。
        
* 複雜度
    * 時間複雜度: O(C + U + min(U^2, N))，因為 C 為最大，因此為 O(C)
    * 空間複雜度: O(1) 或 O(U + min(U^2, N))
    * 備註：C 代表所有單詞總長度、U 是獨特字母的數量、N 為字符串的總數

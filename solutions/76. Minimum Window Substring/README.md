# Minimum Window Substring
[題目連結](https://leetcode.com/problems/minimum-window-substring/)

## 題目描述
原文：

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring**
 of `s` such that every character in t (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.


----

GPT 4 翻譯：

給定兩個分別長度為 `m` 和 `n` 的字符串 `s` 和 `t`，返回 `s` 的**最小窗口子串**，使得 `t` 中的每個字符（**包括重複字符**）都包含在窗口中。如果沒有這樣的子串，則返回空字符串 `""`。

測試案例將會生成一個**唯一的**答案。


----

Example 1

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

Example 2
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

Example 3

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

Constraints:

* `m == s.length`
* `n == t.length`
* `1 <= m, n <= 10^5`
* `s` and `t` consist of uppercase and lowercase English letters.
 

## 思路

做過第 [3](../3.%20Longest%20Substring%20Without%20Repeating%20Characters/) 題和第 [424](../424.%20Longest%20Repeating%20Character%20Replacement/) 題的話，可能會覺得這題也有點像，這題暴力解一樣是找出所有的 Pair 並且找出來後去比較這個區間是否包含 `t`，最後把這些合法的 Pair 算出最短的路徑，複雜度一樣至少 O(N^2)，如果判斷「是否包含 `t`」這邊沒寫好的話，甚至可能到 O(N^3)。

這題一樣用演算法的思維來觀察題目：  
Input: s = "ADOBECODEBANC", t = "ABC"  
在框選時，要框到至少包含 `t` 出現的字母數量。  
當 i = 0 ， **A** DOBECODEBANC  
當 i = 1 ， **AD** OBECODEBANC  
當 i = 2 ， **ADO** BECODEBANC  
當 i = 3 ， **ADOB** ECODEBANC  
當 i = 4 ， **ADOBE** CODEBANC  
當 i = 5 ， **ADOBEC** ODEBANC ✅ 包含了 `t`  

一但發現包含了 `t` ，左邊端點就會開始嘗試往後面走，直到不合法為止，而以現在這個節點而言，左端點走一格後發現不包含 `t` 因此停下來。

當 i = 5 ， A **DOBEC** ODEBANC  
當 i = 6 ， A **DOBECO** DEBANC  
當 i = 7 ， A **DOBECOD** EBANC  
當 i = 8 ， A **DOBECODE** BANC  
當 i = 9 ， A **DOBECODEB** ANC  
當 i = 10， A **DOBECODEBA** NC ✅   

一但區間內又包含 `t` 的時候，`left` 就會開始往後移動，直到又不合法為止。  

當 i = 10， ADOBEC **ODEBA** NC   
當 i = 11， ADOBEC **ODEBAN** C  
當 i = 12， ADOBEC **ODEBANC**  ✅ 修正如下  
當 i = 12， ADOBECODEB **ANC**   

備註：需要將每一次合法時的區間記住，這樣最後就可以找出最小的區間出來。

**方法 1: Sliding Window + HashMap**

* 步驟
    1. 初始化 `slow` 和 `fast` 指標
    2. `fast` 每一次往後走一格，並把 `s[fast]` 在 HashMap 中的次數 +1。
    3. `slow` 只要區間合法包含 `t` 就會往後走，直到不合法為止。

* 複雜度
    * 時間複雜度: O(|S| + |T|)
    * 空間複雜度: O(|S| + |T|)
    * 備註：S 表示字串 `s` 的長度、T 表示字串 `t` 的長度。

**方法 2: Sliding Window + HashMap（優化版）**

當我們上面在 Dry running 的時候，是不是有發現左端點移動的很慢，所以當 `s` 很長， `t` 很短的時候，其實浪費了很多時間在做不必要的運算，因此有一個比較好的方法如下：

Input: s = "ABCDDDDDDEEAFFBC", t = "ABC"  
new_s = `[(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]`  
這個時候 Sliding Window 就不用針對原本的 `s` ，而是 `new_s`，效果是一樣的，而且速度又更快。

* 步驟
    1. 初始化 `s`，轉換成 `new_s: List[Tuple(int, str)]` 的形式
    2. 用 Sliding Window 掃過 `new_s`
    3. 條件跟上一個做法一樣：
        * `fast` 每一次走一格，一但包含 `t` ，長度即為 `new_s[fast][0] - new_s[slow][0] + 1` ，並將區段記錄下來，最後要取出最小的。
        * 只要合法， `slow` 就會試圖往後面走，直到不合法為止。

* 複雜度
    * 時間複雜度: O(|S| + |T|)
    * 空間複雜度: O(|S| + |T|)
    * 備註：S 表示字串 `s` 的長度、T 表示字串 `t` 的長度。

# Valid Palindrome
[題目連結](https://leetcode.com/problems/valid-palindrome/)

## 題目描述
原文：

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

----

GPT 4 翻譯：

如果一個短語在將所有大寫字母轉換成小寫字母並移除所有非字母數字字符後，從前向後和從後向前讀起來都相同，那麼這個短語就是一個**回文**。字母數字字符包括字母和數字。

給定一個字串 `s`，如果它是一個**回文**，則返回 `true`，否則返回 `false`。

----

Example 1
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

Example 2
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
Example 3
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

Constraints:

* `1 <= s.length <= 2 * 10^5`
* `s` consists only of printable ASCII characters.

## 思路

回文我們從小就會，像是「讀書不忘救國，救國不忘讀書。」但這題的回文，不是針對單詞（Word）而是針對字母 (Character)，而且是 Case Insensitive，表示：大寫 A 和 小寫 a 是一樣的。所以只要有辦法跳過特殊符號，只專注在英文、數字就好，整理過後再來比對是否有回文，就沒問題了！

**方法: Reverse**

* 步驟
    1. 重新整理字串：用一個 For Loop 掃過，把英文和數字加入字串中，英文需要轉成小寫。
    2. 判斷 ans == ans[::-1]  # 正序是否等於倒序

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)


有沒有什麼辦法再壓低空間或時間？是有的，回文有一個特性，就是會有兩個指標，一個在前，一個在後，兩兩比對，剛好非常適合用 Two Pointer 來解決，方法如下：

**方法: Two Pointer**
利用左右型的 Two Pointer ，left 放在字串最前面、right 放在字串最後面，比較兩者的小寫是否相同，前進的依據是：如果遇到特殊符號，就往前進。

備註：Two Pointer 的題型關鍵在於，什麼時候指標要移動、以及怎麼移動，這是需要注意的。

* 步驟
    1. 初始化指標 left, right
    2. 移動指標
        - left 往後走，直到遇到數字或英文字
        - right 往前走，直到遇到數字或英文字
    3. 比較 left.lower() 是否等於 right.lower()

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(1)

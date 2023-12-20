# Group Anagrams
[題目連結](https://leetcode.com/problems/group-anagrams/)

## 題目描述
原文：

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

----

GPT 4 翻譯：

給定一個字符串陣列 strs，將 Anagram 分組在一起。你可以以任何順序返回答案。

Anagram 是通過重新排列不同單詞或短語的字母形成的單詞或短語，通常恰好使用所有原始字母一次。


----

Example 1
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

Example 2
```
Input: strs = [""]
Output: [[""]]
```
Example 3
```
Input: strs = ["a"]
Output: [["a"]]
```

Constraints:

* `1 <= strs.length <= 10^4`
* `0 <= strs[i].length <= 100`
* `strs[i]` consists of lowercase English letters.

## 思路

這題是 [242. Valid Anagrams](../242.%20Valid%20Anagram/) 的延伸題，從上一題我們知道，可以透過計算每個字母出現的次數，來判斷兩字串是否為 Anagram，而至少就需要 O(K) 的時間複雜度，K 表示最長字串的長度；而這題要再多做一個分群，多做這一個分群會做多少事呢？要做的事情不只是兩個字串了，而是 N 個字串，所以時間複雜度至少要再一個 O(N)；而為了要將之分群，空間複雜度也會需要 O(NK)。

**方法: Hashmap**

* 步驟
    1. 先用一個迴圈，跑過每一個字串。
    2. 再用一個迴圈，去計算每一個字串字母出現的次數。
    3. 將各字母出現的次數，按照順序放入 Hashmap 當作 Key 值，再把該字串添加到 List 中。

* 複雜度
    * 時間複雜度: O(NK)
    * 空間複雜度: O(NK)


看到這裡是否覺得毛毛的呢？ 對的，因為有一個關鍵字「將各字母出現的次數，按照『順序』放入 Hashmap」，請問這個順序要怎麼建立？

1. 如果是真的將字母先排序，舉例來說:
    ```
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    ans = {
        ("a", "e", "t"): ["eat", "tea", "ate"],
        ("a", "n", "t"): ["tan", "nat"],
        ("a", "b", "t"): ["bat"]
    }
    ```
    排序過後，才有辦法對應到相同的 Key 值，而這件事就需要 O(KlogK) 的時間。

2. 更好的做法：用 List 來做
    * [242. Valid Anagrams](../242.%20Valid%20Anagram/) 有提到，除了用 Hashmap 來儲存字母出現次數以外，也可以用陣列來儲存，因為字母只有 26 個。
    * 而這樣做的好處，可以直接讓順序性直接建立起來，而不用再排序，會得到：
    ```
    ans = {
        ((1, 0, 0, 0, 1, ...)): ["eat", "tea", "ate"],
        ((1, 0, 0, 0, 0, ...)): ["tan", "nat"],
        ((1, 1, 0, 0, 0, ...)): ["bat"]
    }
    ```
    所以用這個做法，才能真正將時間複雜度降到 O(NK)。
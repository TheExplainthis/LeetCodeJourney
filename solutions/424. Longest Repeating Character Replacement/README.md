# Longest Repeating Character Replacement

[題目連結](https://leetcode.com/problems/longest-repeating-character-replacement/)

## 題目描述
原文：

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

----

GPT 4 翻譯：

給定一個字符串 `s` 和一個整數 `k`。你可以選擇字符串中的任何字符並將其更改為任何其他大寫英文字母。你最多可以進行 `k` 次這樣的操作。

返回在執行上述操作後，你能獲得包含相同字母的最長子串的長度。


----

Example 1
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

Example 2
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

Constraints:

* `1 <= s.length <= 10^5`
* `s` consists of only uppercase English letters.
* `0 <= k <= s.length`


## 思路

一樣利用暴力解的思維，就是把每一個 Pair 找出來（"AA", "AAB", "AABA", ...），再針對所有的 Pair 剔除掉不合格的，剩下來的字串再來找出最長的，就可以做完，但這樣的做法太慢了，需要 O(N^2)，而且仔細觀察，會重複計算大量不必要的運算，為了能夠加快，我們可以試著用演算法的做法，拿出一支筆，從左到右開始畫粗體：  

Input: s = "AABABBA", k = 1  
當 i = 0， **A** ABABBA  
當 i = 1， **AA** BABBA  
當 i = 2， **AAB** ABBA  

畫到這裡要手抖一下，因為遇到不同的字母 B，但因為我們有一次修改的機會 (k = 1)，所以仍然可以容忍。  

當 i = 3， **AABA** BBA  
當 i = 4， **AABAB** BA  

此時又遇到了一個 B，但我們能替換的額度已經沒了，所以這個字串是不可行的，這時後字串選範圍就要往右邊移，如下：  

當 i = 4， A **ABAB** BA  # 仍然不合法，需要再移動  
當 i = 4， AA **BAB** BA  # 合法，只有 A 一個字母不同，繼續往下  
當 i = 5， AA **BABB** A  
當 i = 6， AA **BABBA**   # 不合法，需移動框  
當 i = 6， AABA **BBA**   ## 合法，只有 A 一個字母不同  


**方法 1: 利用 Sliding Window + HashMap**

* 步驟
    1. 初始化 `slow`, `fast`, `freq_map = {}`
    2. `slow` 和 `fast` 前進的條件是？
        - `fast`: 每一次走一步，把新的字母加進來試試看。
        - `slow`: 如果加入 `fast` 所在的字母進來後發現：`（字串總長度 - 重複最多的字母數）> k` 代表超出替換的扣打，這時後 `slow` 就要開始往前移動直到變成合法：
        ```python
        # fast - slow + 1 -> 字串長度
        # max(freq_map.values()) -> 最高頻出現的字母次數
        while ((fast - slow + 1) - max(freq_map.values())) > k:
            freq_map[s[slow]] -= 1
            slow += 1
        ```
        
* 複雜度
    * 時間複雜度: O(NM)   
    * 空間複雜度: O(M)
    * 備註：N 為字串長度，M 為字母數最多為 26


**方法 2: 利用 Sliding Window + HashMap (優化版)**

在看到 `max(buckets.values())` 的時候，就可以去想這一段是不是可再優化，因為這一個時間複雜度需要 O(M) 的時間，但他最主要的目的其實就只是找出最高頻出現的字母次數，那能不能用別的方法做呢？是有的，再多用一個變數名稱，記住當前最高頻的次數即可！

* 步驟
    1. 初始化 `slow`, `fast`, `seen = {}`, `max_freq`
    2. `slow` 和 `fast` 前進的條件是？
        - `fast`: 每一次走一步，把新的字母加進來試試看。
        - `slow`: 如果加入 `fast` 所在的字母進來後發現：（字串總長度 - 重複最多的字母數）> k 代表超出替換的扣打，這時後 `slow` 只要往前走一格就好，他往前走一格後，必然會讓上面的式子成立。
        ```python
        freq_map[s[fast]] = freq_map.get(s[fast], 0) + 1 
        max_freq = max(max_freq, freq_map[s[fast]])

        if (fast - slow + 1) - max_freq > k:
            freq_map[s[slow]] -= 1
            slow += 1
        ```

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(M)
    * 備註：N 為字串長度，M 為字母數最多為 26


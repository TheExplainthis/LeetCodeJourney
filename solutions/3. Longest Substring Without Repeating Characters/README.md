# Longest Substring Without Repeating Characters

[題目連結](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 題目描述
原文：

Given a string `s`, find the length of the longest 
substring without repeating characters.

----

GPT 4 翻譯：

給定一個字符串 `s`，找出最長的不含重複字符的子串的長度。

----

Example 1
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

* `0 <= s.length <= 5 * 10^4`
* `s` consists of English letters, digits, symbols and spaces.


## 思路

先用暴力解的思維，就是把每一個 Pair 找出來（"a", "ab", "abc", ...），再針對所有的 Pair 剔除掉不合格的，剩下來的字串再來找出最長的，就可以做完，但這樣的做法太慢了，需要 O(N^3)，而且仔細觀察，會重複計算大量不必要的運算，為了能夠加快，我們可以試著用演算法的做法，拿出一支筆，從左到右開始畫：  

Input: s = "abcabcbb"  
當 i = 0， <u>a</u>bcabcbb  
當 i = 1， <u>ab</u>cabcbb  
當 i = 2， <u>abc</u>abcbb  
當 i = 3， <u>abca</u>bcbb  
畫到這裡要手抖一下，因為 a 已經重複了，這時候可能的做法是，放棄前面的 a，所以再一次：  
當 i = 3， a<u>bca</u>bcbb  
當 i = 4， a<u>bcab</u>cbb  
b 又重複了改成，又將最前面的 b 放棄，就這樣以此類推的往下做就有機會可以做完！  
當 i = 4， ab<u>cab</u>cbb  
當 i = 5， abc<u>abc</u>bb  
當 i = 6， abcab<u>cb</u>b  
當 i = 6， abcabcb<u>b</u>  

等等，這怎麼可能想的到！對的，因為要像是計算機一樣的思考，會有點困難，所以這是需要訓練的！不擔心，我們有一天會訓練起來的！  

上面的方法就是標準的 Sliding Window 題型，要判斷 `slow` 和 `fast` 之間個字母出現的次數，可以利用 Set 或者 HashMap 來處理，我們下面可以比較一下差異：

**方法 1: 利用 Sliding Window + Set**

* 步驟
    1. 初始化 `slow`, `fast`, `seen = set()`
    2. `slow` 和 `fast` 前進的條件是？
        - `fast`: 每一次走一步，把新的字母加進來試試看。
        - `slow`: 如果加入 `fast` 所在的字母進來後發現有重複，`slow` 就必須往前走，直到沒重複為止。
        
* 複雜度
    * 時間複雜度: O(N)   
    * 空間複雜度: O(min(N, M))
    * 備註：N 為字串長度，M 為字母數


**方法 2: 利用 Sliding Window + HashMap**

方法 1，`left` 每一次只會往前走一格，有沒有辦法讓他用跳躍的方式，一次略過那些重複的狀況，這時後就可以用 HashMap 了，他可以順便記住每個字母出現的位置，當 `right` 前進發現重複後，`left` 會跳到該字母過去出現過的位置 + 1 的地方，就可以保證這個區段內是不重複的。

* 步驟
    1. 初始化 `slow`, `fast`, `seen = {}`
    2. `slow` 和 `fast` 前進的條件是？
        - `fast`: 每一次走一步，把新的字母加進來試試看。
        - `slow`: 如果加入 `fast` 所在的字母進來後發現有重複，`slow` 就去到過往重複字母所在位置的下一格
    3. 計算 `fast` 到 `slow` 之間的距離

* 複雜度
    * 時間複雜度: O(N)   # 會比方法 1 再更快一點，但複雜度一樣
    * 空間複雜度: O(min(N, M))
    * 備註：N 為字串長度，M 為字母數


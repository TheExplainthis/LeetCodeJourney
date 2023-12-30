# Valid Parentheses
[題目連結](https://leetcode.com/problems/valid-parentheses/)

## 題目描述
原文：

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


----

GPT 4 翻譯：

給定一個只包含字符 '('、')'、'{'、'}'、'[' 和 ']' 的字符串 s，判斷輸入的字符串是否有效。

一個輸入字符串是有效的，如果滿足以下條件：

1. 開放的括號必須由相同類型的括號關閉。
2. 開放的括號必須按正確的順序關閉。
3. 每一個關閉的括號都有一個對應的相同類型的開放括號。

----

Example 1
```
Input: s = "()"
Output: true
```

Example 2
```
Input: s = "()[]{}"
Output: true
```

Example 3
```
Input: s = "(]"
Output: false
```

Constraints:

* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`

## 思路

何謂合法的括號，先用人類的方式來判斷，：  
✅ `[[]]`　有效  
❌ `[[]`　 無效規則 1，因為少了 `]`  
❌ `][`　　無效規則 2，因為 `]` 之前沒有 `[`  
❌ `[(])`　無效規則 3，因為括號穿插。  

以演算法的思維來看，我們先來看看這個例子  
Input: `s = "([]])"`  
⚠️，i = 0，`(`  
⚠️，i = 1，`([`  
✅，i = 2，`([]`　　　　 # 遇到 `]` ，對應前方的 `[`  
❌，i = 3，`([]]`　　　　# 遇到 `]` ，前方無 `[`  

如果今天把所有左括號，包含 `(`、`[`、`{` 出現的地方，都標注一個位置，迴圈後面遇到右括號時 `)`、`]`、`}`，再回去找他對應的左括號位置，感覺是有機會的，我們嘗試用 HashMap 來做，可能會變成下面：  

`s = "([]])"`  
i = 0，`hashmap = {0: '('}`  
i = 1，`hashmap = {0: '(', 1: '['}`  
i = 2 碰到 `]` 的時候，就要從 `hashmap` 去回頭看，但因為 `hashmap` 沒有順序性，所以沒辦法回頭看，因此 HashMap 並不適合，換成 Array 試試看：

`s = "([]])"`  
i = 0，`array = ['(']`  
i = 1，`array = ['(', '[']`  
i = 2 碰到 `]` 的時候，就要從 `array` 去回頭看：
從 `array[-1]` 的找到 `[` -> ✅ 有效，並且移除尾巴元素 `[`，此時 `array = ['(']`

i = 3 碰到 `]` 的時候，就要從 `array` 去回頭看：  
從 `array[-1]` 不是 `[` -> ❌ 無效，遇到其他左括號 `(`，則返回 `False`

--

感覺以上做法蠻可行的，用一個 Array 就可以，而這個 Array 的操作特性是，要從尾巴放進去、從尾巴拿出來判斷，這個資料結構有一個新的名詞，叫做 Stack，所以把上面的例子改寫一下，變成：

`s = "([]])"`  
i = 0，`stack = ['(']`  
i = 1，`stack = ['(', '[']`  

i = 2 碰到 `]` 的時候，就要從 stack 去回頭看：  
從 stack 的最尾巴往前找到 `[` -> ✅ 有效並且移除尾巴元素 `[`  

i = 3 碰到 `]` 的時候，就要從 stack 去回頭看：  
從 `stack = ['(']` 的尾巴往前找 -> ❌ 無效，遇到其他左括號

**方法 1: Stack**

* 步驟
    1. 用迴圈掃過陣列。
        - 當遇到左括號時，將符號 push 到 Stack 中。
        - 當遇到右括號時，Stack 為尾巴的地方是否存在對應的左括號
            - 存在：將左括號 pop 出來
            - 不存在：返回 `False`
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)

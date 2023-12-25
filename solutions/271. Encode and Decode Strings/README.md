# Encode and Decode Strings
[題目連結](https://leetcode.com/problems/encode-and-decode-strings/)

## 題目描述
原文 + GPT-4 翻譯：

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

設計一個演算法來將一串字串編碼成一個字串。這個編碼後的字串隨後透過網路傳送，並被解碼回原始的字串列表。

Machine 1 (sender) has the function:

機器 1（發送方）有以下函式：

```cpp
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

Machine 2 (receiver) has the function:

機器 2（接收方）有以下函式：

```cpp
vector<string> decode(string s) {
  //... your code
  return strs;
}
```

So Machine 1 does:

因此機器 1 執行：

```cpp
string encoded_string = encode(strs);
```

and Machine 2 does:

而機器 2 執行：

```cpp
vector<string> strs2 = decode(encoded_string);
```

strs2 in Machine 2 should be the same as strs in Machine 1.

機器 2 中的 strs2 應與機器 1 中的 strs 相同。

Implement the encode and decode methods.

請實作 encode 和 decode 方法。

You are not allowed to solve the problem using any serialize methods (such as eval).

你不可以使用任何序列化方法（如 eval）來解決這個問題。

----

Example 1:
```
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

Example 2:
```
Input: dummy_input = [""]
Output: [""]
```

## 思路

這題有一個簡單的做法，就是如果有辦法用一個很特殊的字元或字串，Encode 時來當作字串與字串之間的分隔號，Decode 時再以這個分隔號重新切成陣列，就可以完成。


**方法 1: 利用「特殊符號」**

* 步驟
    1. Encode 利用特殊符號「π」來當作字串與字串之間的分隔號
        ```python
        'π'.join(strs)
        ```

    2. Decode 利用「π」這個分隔號來切陣列
        ```python
        s.split('π')
        ```

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(K)
    * 備註：N 表示所以字串組合後總長度，K 表陣列長度

**方法 2: Escaping**

這題實際上是在學這個概念 Escaping，方法 1 很有可能在文本當中有各式各樣的文字，包含特殊字元，因此可能會讓演算法失效，因此要想一個一定可行的方法，這邊可以參考目前計算機領域都在使用的方法，像是 python 會用 \\n 來表示換行，做法類似。

Escaping 的概念在於，可以在 Encode 時，將看到的字符做「轉譯」，舉例來說：
```python
strs = ["Hello", "World"]
"/:".join(strs)   // Hello/:World
```
但是當文字出現預設的分隔號時就會出錯，如下：
```python
strs = ["Hello", "Wor/:ld"]
"/:".join(strs)   // Hello/:Wor/:ld 
```

所以要做的事情是，先將 strs 裡面的字串，如果出現特殊符號時就先轉意，如下：
```python
strs = ["Hello", "Wor/:ld"]
new_strs = ["Hello", "Wor//:ld"]
"/:".join(strs)   // Hello/:Wor//:ld 
```
所以如果 Decode 時看到 `/:` 就代表是分隔號，如果看到 `//:` 就代表原本的字串中有 `/:`。

* 步驟
    1. Encode 先針對所有字串做 Escaping、在把字串串在一起。
    2. Decode 時，先去找是否有 Escaping 的字符，再做處理。

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(K)
    * 備註：N 表示所以字串組合後總長度，K 表陣列長度

# Implement Trie (Prefix Tree)

[題目連結](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

## 題目描述
原文：

A trie (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

* `Trie()` Initializes the trie object.
* `void insert(String word)` Inserts the string `word` into the trie.
* `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
* `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

----

GPT 4 翻譯：

一個字典樹（發音為 "try"）或**前綴樹**是一種樹狀數據結構，用於高效地儲存和檢索字符串數據集中的鍵。這種數據結構有各種應用，例如自動完成和拼寫檢查。

實現 Trie 類別：

* `Trie()` 初始化 trie 對象。
* `void insert(String word)` 將字符串 `word` 插入到 trie 中。
* `boolean search(String word)` 如果字符串 `word` 在 trie 中（即之前已插入），則返回 `true`，否則返回 `false`。
* `boolean startsWith(String prefix)` 如果存在一個先前插入的字符串 `word`，它有前綴 prefix，則返回 `true`，否則返回 `false`。

----

Example 1
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

```

Constraints:

* `1 <= word.length, prefix.length <= 2000`
* `word` and `prefix` consist only of lowercase English letters.
* At most `3 * 10^4` calls **in total** will be made to `insert`, `search`, and `startsWith`.

## 思路

Trie 的結構：
* 節點結構：每個節點代表一個字母。除了根節點外，每個節點都與一個字母相關聯。
* 子節點鏈接：每個節點包含多個鏈接（通常是一個固定大小的陣列，大小等於字母表中的字母數量），每個鏈接對應到字母表中的下一個字母。
* 終止標記：每個節點應該有一個標記來指示是否有單詞在該節點結束。

Trie 類別的方法實現:
* 初始化 (`Trie()`)
    * 創建一個根節點，這個節點不包含字母，但它將包含指向其他字母的鏈接。
  
* 插入 (`void insert(String word)`)
  * 從根節點開始，對於 `word` 中的每個字母，沿著字典樹下移動。
  * 如果當前字母的鏈接不存在，創建一個新節點。
  * 移動到這個節點，然後繼續處理下一個字母。
  * 在單詞的最後一個字母處，標記終止節點。

* 搜索 (`boolean search(String word)`)
  * 從根節點開始，沿著 word 的每個字母下移動。
  * 如果任何時候字母的鏈接不存在，返回 `false`。
  * 如果所有字母都找到且最後一個字母標記為終止，則返回 `true`。

* 前綴搜索 (`boolean startsWith(String prefix)`)
  * 這與 search 方法類似，但即使最後一個字母不是終止標記，只要所有字母都在字典樹中，就返回 `true`。


## 複雜度
* 插入
  * 時間複雜度: O(M)
  * 空間複雜度: O(M)
* 搜尋
  * 時間複雜度: O(M)
  * 空間複雜度: O(1)
* 前綴搜索
  * 時間複雜度: O(M)
  * 空間複雜度: O(1)
備註：其中 M 為 `word` 長度

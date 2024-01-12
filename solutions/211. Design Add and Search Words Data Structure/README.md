# Design Add and Search Words Data Structure

[題目連結](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)

## 題目描述
原文：

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

* `WordDictionary()` Initializes the object.
* `void addWord(word)` Adds `word` to the data structure, it can be matched later.
* `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.


----

GPT 4 翻譯：

設計一個資料結構，支持添加新單詞和查找字符串是否匹配任何先前添加的單詞。

實現 `WordDictionary` 類別：

* `WordDictionary()` 初始化對象。
* `void addWord(word)` 將 `word` 添加到資料結構中，稍後可以進行匹配。
* `bool search(word)` 如果資料結構中有任何字符串與 `word` 匹配，則返回 `true`；否則返回 `false`。`word` 中可能包含點 `'.'`，點可以與任何字母匹配。

----

Example 1:
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```


Constraints:

* `1 <= word.length <= 25`
* `word` in `addWord` consists of lowercase English letters.
* `word` in `search` consist of `'.'` or lowercase English letters.
* There will be at most `2` dots in `word` for `search` queries.
* At most `10^4` calls will be made to `addWord` and `search`.

## 思路

通常面對字典的題型，都會使用 Trie 來儲存單詞。字典樹是一種用於快速查詢前綴的樹狀結構，非常適合於此類問題。

* 初始化：
  * `WordDictionary()`：初始化字典樹的根節點。
* 新增單詞：
  * `addWord(word)`：從根節點開始，按照單詞 `word` 中的每個字母依次在字典樹中插入。如果該字母的節點不存在，則創建一個新節點。
* 查詢單詞：
  * search(word)：這是最複雜的部分。需要從根節點開始，按字母查詢字典樹。
  * 對於普通字母，直接移動到對應的子節點。
  * 對於點（'.'），需要考慮所有可能的子節點（即該節點的所有子節點），並對每個子節點進行遞迴搜索。
  * 如果到達單詞末尾，檢查當前節點是否標記為一個完整單詞的結尾。
* 實現細節：
  * 字典樹的每個節點可以使用一個固定大小的數組（對於小寫字母 a-z，大小為 26）來表示子節點，或者使用映射（如哈希表）來節省空間。
  * 需要一個額外的標記在每個節點上，表示該節點是否是某個單詞的結尾。

## 複雜度
* 新增單詞
  * 時間複雜度: O(M)
  * 空間複雜度: O(M)

* 查詢單詞
    * 時間複雜度: O(NlogN)
      * 如果字串中無任何的 `'.'`，則為 O(M)。 (最優)
      * 如果字串中全部都是 `'.'`，則為 O(N * 26^M)。 (最糟)
    * 空間複雜度:
      * 如果字串中無任何的 `'.'`，則為 O(1)。 (最優)
      * 如果字串中全部都是 `'.'`，則為 O(M)。 (最糟)
備註：其中 M 為 `word` 長度，N 為所有 key 的個數。

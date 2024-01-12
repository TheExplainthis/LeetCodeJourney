# Serialize and Deserialize Binary Tree

[題目連結](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)

## 題目描述
原文：

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification**: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

----

GPT 4 翻譯：

序列化是將數據結構或對象轉換成位元序列的過程，使其能夠存儲在文件或內存緩衝區中，或通過網絡連接鏈路傳輸，以便稍後在相同或另一個計算機環境中重建。

設計一個算法來序列化和反序列化二元樹。你的序列化/反序列化算法如何運作沒有限制。你只需要確保一棵二元樹可以被序列化為字符串，並且這個字符串可以被反序列化為原始樹結構。

**澄清**：輸入/輸出格式與 LeetCode 序列化二元樹的方式相同。你不必一定遵循這種格式，請發揮創意，自己想出不同的方法。

----

Example 1

![Example 1](example1.jpeg)

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

Example 2

```
Input: root = []
Output: []
```

Constraints:

* The number of nodes in the tree is in the range `[0, 10^4]`.
* `-1000 <= Node.val <= 1000`

## 思路

我們之前提過，單獨一個遍歷方式（preorder, inorder, postorder, level order）都無法重新建構出一顆唯一的樹，但是在 [572. Subtree of Another Tree](../572.%20Subtree%20of%20Another%20Tree/) 又知道說，如果能調整一下，其實是可以的。因此我們可有兩種做法：  
1️⃣ 將一棵樹做 preorder 和 inorder ，並將兩結果用符號 `,` 隔開，要重新建回樹的時候，再依據 `,` 來分回兩半。  
2️⃣ 572 題有說，因為空節點都沒有任何標記，才會導致這樣的狀況，所以把空節點也用一個符號表示，這樣一個遍歷就可以解決。

**方法: Recursive**

* 步驟
    1. serialize：
       1. 將樹用 preorder 的做法但是遇到空節點時要額外加上特殊符號。
       2. 回傳時用 `,` 將元素串在一起。
    2. deserialize：
       1. 利用 `,` 來分割字串，變回陣列。
       2. 再用 dfs 把樹建回來，建立的時候：
          1. 若 dfs 遇到空節點的特殊符號就跳過，回傳 None 即可。
          2. 若非空節點就將其元素建立成節點 node = TreeNode(val)
             1. node.left = dfs() # 繼續往下遞迴
             2. node.right = dfs()
        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)
      * 為了加快搜尋速度，會先將 inorder 序列儲存在 Hashmap 裡 -> O(N)
      * 樹在遞迴的平均高度為 logN -> O(logN)

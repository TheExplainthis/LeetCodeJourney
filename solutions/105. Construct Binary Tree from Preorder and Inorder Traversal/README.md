# Construct Binary Tree from Preorder and Inorder Traversal

[題目連結](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

## 題目描述
原文：

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

----

GPT 4 翻譯：

給定兩個整數數組 `preorder` 和 `inorder`，其中 `preorder` 是一棵二元樹的前序遍歷，而 `inorder` 是同一棵樹的中序遍歷，構建並返回該二元樹。

----

Example 1

![Example 1](example1.jpeg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

Example 2

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]

```

Constraints:

* `1 <= preorder.length <= 3000`
* `inorder.length == preorder.length`
* `-3000 <= preorder[i], inorder[i] <= 3000`
* `preorder` and `inorder` consist of **unique** values.
* Each value of `inorder` also appears in `preorder`.
* `preorder` is **guaranteed** to be the preorder traversal of the tree.
* `inorder` is **guaranteed** to be the inorder traversal of the tree.


## 思路

單獨一個 preorder 或 inorder 序列並不能構成唯一個樹，但如果同時給了這兩個序列就可以，而可以觀察一下這兩個序列，以 Example 1 為例，preorder 的第一個節點 `3` 會是根節點，並且對應到 inorder 第 `index=1` 的位置，而 inorder 的特性剛好可以樹一分為二，代表 `index < 1` 的部分都是左子樹、`index > 1` 的部分都是右子樹。

所以，我們每一次從 preorder 拿一個節點出來，知道根節點為何，再拿去對應 inorder 序列，知道要從哪裡一分為二，不斷地遞迴下去。


**方法: Recursive**

* 步驟
    1. 建立一個 recursive 函式：
       1. Base Case: 當沒節點可挑時
       2. Recusive Case:
          1. node.left = dfs(起點, 一分為二的點 - 1)
          2. node.left = dfs(一分為二的點 + 1, 終點)

        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)
      * 為了加快搜尋速度，會先將 inorder 序列儲存在 Hashmap 裡 -> O(N)
      * 樹在遞迴的平均高度為 logN -> O(logN)

# Kth Smallest Element in a BST

[題目連結](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

## 題目描述
原文：

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (**1-indexed**) of all the values of the nodes in the tree.

----

GPT 4 翻譯：

給定一個二元搜尋樹的 `root`，和一個整數 `k`，返回樹中所有節點值的第 k 小的值（**1 索引**）。

----

Example 1


![Example 1](example1.jpeg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

Example 2

![Example 2](example2.jpeg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```


Constraints:

* The number of nodes in the tree is `n`.
* `1 <= k <= n <= 10^4`
* `0 <= Node.val <= 10^4`

## 思路

感覺可以利用 BST 的特性，只要用一次 Inorder，就能找到小到大的順序，再吐回第 k 個位置，那就可以找到答案，而這樣的複雜度為 O(N)，空間複雜度是 O(logN)，有沒有可能更低的複雜度呢？  
試想一下，如果要更低，那就只剩下 O(logN) 的可能，也就是 Binary Search 的方法，每一次把樹切一半去找，但這樣可行嗎？感覺不可行，因為根本不知道左子樹和右子樹的數量，所以感覺 O(N) 就是極限了。

**方法 1: Recursive**

* 步驟
    1. 利用 Recursive 來找出 Inorder 的序列。
    2. 返回第 k - 1 個位置（表示第 k 小的數）

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N) # 需要遍歷完全部後才能知道答案


**方法 2: Iterative**

* 步驟
    1. 利用 Iterative + Stack 來找出 Inorder 的序列。
    2. 返回第 k - 1 個位置（表示第 k 小的數）

* 複雜度
    * 時間複雜度: O(h + k) # k 次 pop 的操作
    * 空間複雜度: O(h)
    * h 為樹高，平均狀況為 logN、最糟狀況為 N。


## Follow up
如果這個二元搜索樹經常被修改（即，我們可以進行插入和刪除操作），並且你需要經常找到第 k 小的元素，你會如何進行優化？  

正常的做法，就是就是先插入 O(h) 再搜尋（上面的 Iterative 演算法） O(h + k)，所以總計為 O(2h + k)，如果要加快可以把最後一層葉子全部用 Double Linked List 串在一起，這時後維持樹和搜尋第 k 小就是兩件事了。維持樹只需要 O(h)，找第 k 小可以從 Double Linked List 來找，只需要 O(k)。


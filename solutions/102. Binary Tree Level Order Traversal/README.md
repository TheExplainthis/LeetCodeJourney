# Binary Tree Level Order Traversal

[題目連結](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## 題目描述
原文：

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


----

GPT 4 翻譯：

給定一個二元樹的 `root`，返回其節點值的層次遍歷。（即，從左到右，逐層進行）。

----

Example 1

![Example 1](example1.jpeg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

Example 2

```
Input: root = [1]
Output: [[1]]
```

Example 3

```
Input: root = []
Output: []
```

Constraints:

* The number of nodes in the tree is in the range `[0, 2000]`.
* `-1000 <= Node.val <= 1000`


## 思路:

這題可以看作是第 [104. Maximum Depth of Binary Tree](../104.%20Maximum%20Depth%20of%20Binary%20Tree/) 的延伸，只要將每一層的節點放入該層的陣列中，就可以完成。


**方法 1: Iterative**

用 Iterative 時，建議可以搭配 Queue 來實作，雖然 Queue 在一般狀況下的空間複雜度不如 Stack，但是他實作起來較為直觀。  

除了用 Queue 以外，這題還需要額外用 HashMap 去儲存每一個節點所在的層次。

* 步驟
    1. 將 Queue 做初始化
    2. 將 (root, layer=0) 放入 Queue 中
    3. 每一次從 Queue 中取一個 (節點, layer) 出來，將其放入對應的 HashMap 層當中。

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)

**方法 2: Recursive**

Base Case: None 如果 root 是 None  
Recursive Case:  
左邊節點：(root.left, layer + 1)  
右邊節點：(root.right, layer + 1)   

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)


# Invert Binary Tree

[題目連結](https://leetcode.com/problems/invert-binary-tree/)

## 題目描述
原文：

Given the `root` of a binary tree, invert the tree, and return its *root*.

----

GPT 4 翻譯：

給定一個二元樹的 `root`，翻轉這棵樹，並返回它的*根節點*。

----

Example 1

![Example 1](example1.jpeg)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

Example 2

![Example 2](example2.jpeg)

```
Input: root = [2,1,3]
Output: [2,3,1]
```

Example 3
```
Input: root = []
Output: []
```

Constraints:

* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`


## 思路

這題的思路單純，只要把每一個節點的左右交換，遞迴的做下去，就能做完。

**方法 1: Recursive**

* 步驟
    1. Base Case: 當該節點為空時，就回傳空（None）。
    2. Recursive Case:
        - 左、右各別做遞迴：
            - right = self.invertTree(root.right)
            - left = self.invertTree(root.left)
        - 交換：
            - root.left = right
            - root.right = left
        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(h)   # h 表樹的高度，平均來說為 O(logN)

**方法 2: Iterative**

若要用 Iterative 來訪問子節點，就必須要先把節點都先存在某個地方，再取出來處理。這邊可以用 Queue、Stack 都是可以的，實作上都差不多難度，不過複雜度是有差的，詳細可以參考 [104. Maximum Depth of Binary Tree](../104.%20Maximum%20Depth%20of%20Binary%20Tree/) 題，而我們這邊選用 Stack 效果會較好。


* 步驟
    1. 選一個記憶區 Stack
    2. 先把根部節點 root 丟入 stack 中
    3. 每一次從 stack 中取一個節點出來
        - 將其左子節點與右子節點交換
        - 並將左、右子節點也放入 Stack 中，等待之後被取用。
        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(h)   # h 表樹的高度，平均來說為 O(logN)

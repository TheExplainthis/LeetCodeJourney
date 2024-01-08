# Same Tree

[題目連結](https://leetcode.com/problems/same-tree/)

## 題目描述
原文：

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



----

GPT 4 翻譯：

給定兩個二叉樹的根節點 `p` 和 `q`，編寫一個函數來檢查它們是否相同。

如果兩個二叉樹在結構上相同，且節點具有相同的值，則視為相同。

----

Example 1

![Example 1](example1.jpeg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

Example 2

![Example 2](example2.jpeg)

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

Example 3

![Example 3](example3.jpeg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

Constraints:

* The number of nodes in both trees is in the range `[0, 100]`.
* `-10^4 <= Node.val <= 10^4`


## 思路 1: Iterative

要判斷兩個 Tree 是否相同，想像可以用同樣的遍歷方式來遍歷兩棵樹，只要有發現不同就返回 `False`。但要怎麼讓兩棵樹有同樣的遍歷方式呢？用兩個 stack，用同樣的方式 Push、同樣的方式 Pop，就可以有同樣的遍歷方式。

**方法 1: Iterative**

* 步驟
    1. 初始化 p 的 stack 和 q 的 stack。
    2. 將 p 的根節點放入 p 的 stack，q 的根節點放入 stack。
    3. 當兩個 stack 長度都不為 0 時，代表還沒遍歷完：
        * 從 p 的 stack 取一個節點出來、從 q 的 stack 取一個節點出來，兩個做比較。
        * 如果兩節點值不相同就返回 False。
        * 如果相同就個別繼續把左子節點和右子節點放入 stack 中。
    4. 當有一個長度為 0 、有一個不為 0 則代表有一個樹已經遍歷完了，另一個還沒，代表樹束不相同，返回 False。
        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(h)   # h 表樹的高度，平均來說為 O(logN)


## 方法 2: Recursive

如果利用 Recursive 來思考，就必須要去思考 Base Case 和 Recursive Case 可以怎麼設計，先從 Recursive Case 來思考，Tree 的題目可以想的是：能不能夠切成左子樹與右子樹去處理。以本題為例：  
1️⃣ Recursive Case：  
```
return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```
意思是要往上層回傳 `（兩樹根節點值相同）`且`（第一棵樹的左子樹和第二棵樹的左子樹相同）`且`（第一棵樹的右子樹和第二棵樹的右子樹相同）`，三個都成立就回傳 True，有一個不成立就回傳 False。
　
2️⃣ Base Case 終止條件：  
```
如果 （兩樹根節點都是空）就返回 True
如果 （有一個空且另一個不是空） 就返回 False
```

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(h)   # h 表樹的高度，平均來說為 O(logN)

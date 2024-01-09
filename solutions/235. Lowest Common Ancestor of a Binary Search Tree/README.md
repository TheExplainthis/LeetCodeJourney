# Lowest Common Ancestor of a Binary Search Tree

[題目連結](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## 題目描述
原文：

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

----

GPT 4 翻譯：

給定一個二元搜索樹（BST），找出 BST 中兩個給定節點的最低共同祖先（LCA）節點。

根據維基百科上對 LCA 的定義：“最低共同祖先是在兩個節點 `p` 和 `q` 之間定義的，作為 `T` 中同時擁有 `p` 和 `q` 作為後代（我們允許**一個節點是它自己的後代**）的最低節點。”

----

Example 1

![Example 1](example1.png)

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

Example 2

![Example 2](example2.png)

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

Example 3

```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

Constraints:

* The number of nodes in the tree is in the range `[2, 10^5]`.
* `-10^9 <= Node.val <= 10^9`
* All `Node.val` are **unique**.
* `p != q`
* `p` and `q` will exist in the BST.


## 思路:

這題是人類用肉眼看覺得很簡單的題目，但是用演算法就很需要想一下的題目。我們一起來試試看吧： 
Example 1 的圖來看，我們嘗試來用不同的 `p` 和 `q` 來找找規則。  

當 `p = 2, q = 8`  
第一輪: `root = 6`，且 `root > p and root < q`。(結束)  

當 `p = 0, q = 4`  
第一輪: `root = 6`，且 `root > p and root > q`。(往左邊去)  
第二輪: `root = 2`，且 `root > p and root < q`。(結束)  

當 `p = 8, q = 9`  
第一輪: `root = 6`，且 `root < p and root < q`。(往右邊去)  
第二輪: `root = 8`，且 `root = p`。(結束)  

有感覺了嗎？是不是可能是這樣呢？  
從根節點往葉子做 Recursive，拆分成下面四種狀況：  
如果 `root > p and root < q` 返回 `root` (答案)  
如果 `root > p and root > q` 下一輪往 `root.left` 去找  
如果 `root < p and root < q` 下一輪往 `root.right` 去找  
如果 `root = p or root = q` 返回 `root` (答案)  

整理一下是：  
```
if root > p and root > q 下一輪往 root.left 去找
elif root < p and root < q 下一輪往 root.right 去找
else (返回 root)
```

**方法 1: Iterative**

* 步驟
    1. 初始化 stack = [root]
    2. 從 stack 找一個節點出來，判斷其值的範圍
       1. 如果 `root.val > p.val and root.val > q.val` 將 `root.left` 推進 stack。 
       2. 如果 `root.val < p.val and root.val < q.val` 將 `root.right` 推進 stack。 
       3. 其他狀況則返回 `root`
        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(1) # 永遠只有一個節點


**方法 2: Recursive**

* 步驟
    1. 列出函式：
       1. `if root > p and root > q` 下一輪往 `root.left` 去找
       2. `elif root < p and root < q` 下一輪往 `root.right` 去找
       3. `else` (返回 `root`)
          
    
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)

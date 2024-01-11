# Binary Tree Maximum Path Sum

[題目連結](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

## 題目描述
原文：

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum*** of *any **non-empty** path*.


----

GPT 4 翻譯：

在二元樹中的一條**路徑**是由一系列節點組成，其中序列中的每對相鄰節點都透過邊連接在一起。一個節點在序列中最多**只能出現一次**。注意，路徑不需要經過根節點。

一條路徑的**路徑總和**是該路徑上所有節點的值的總和。

給定一個二元樹的 `root`，返回*任何**非空**路徑的最大**路徑總和***。

----

Example 1

![Example 1](example1.jpeg)

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

Example 2

![Example 2](example2.jpeg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

Constraints:

* The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
* `-1000 <= Node.val <= 1000`


## 思路

這種題目在 Tree 的題型特別常見，我稱之為：「會讓你誤以為要轉成 Graph 才能做」的題型。因為看題目敘述，感覺樹明明只能往下層節點去指，但他的題目範例，感覺需要從下層節點往上層節點去指，該怎麼做呢？

這時候需要回過頭來仔細觀察題目，可能有幾種想法可以參考：  
1️⃣ 如果能轉成某一個序列，序列中去看連續的數字加總中，是否有最大值。  
2️⃣ 如果每一個節點可以變成「取」或「不取」的題型。  
3️⃣ 這棵樹如果可以從**葉子節點**開始標記數值，**非葉子節點**則標記其子節點中值較大的那個加上自己。  

如果想法是 1 的話，又看到上面兩個範例，就會感覺好可行，應該就是這樣了，但你只要簡單的把範例 2 的 `-10` 改成 `10`，就知道不可行，因為到 `20` 的時候就分岔了， `15` 和 `7` 只能選一個。但變成序列後會看不出來這件事。 ❌

如果想法是 2，因為他是路徑，所以節點之間需要連續，每一個節點沒辦法單獨判斷自己要取或不取，感覺也不可行。 ❌

第三種難道可以嗎？我們可以觀察到，以範例二為例
1. 從根節點(`-1`)來看，對他來說的最大路徑，就是左邊負的不要，右邊最大是(`20 + 15`) + 自己(`9`)。
2. 再往右子節點(`20`)來看，他的最長路徑是：左子樹的(`15`) + 右子樹的(`7`) + 自己(`20`)。

從以上發現了幾件事：
1. 如果**子樹**數值總和是負的就不取
2. **子樹**再計算數值總和時，並不能有分岔的狀況，像是範例二，對 `10` 而言，右子樹的路徑總和最大值，並非 (`15 + 7 + 20`)，而是 `20` 這個節點再往父節點傳時，只能從子節點中挑一個最大的。

**方法: Recursive**

* 步驟
    1. Base Case: 遇到空節點就回傳 `0`
    2. Recursive Case: 其他狀況則回傳 `max(left, right) + root.val`
        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(h)   # h 表樹的高度，平均來說為 O(logN)，最糟為 O(N)

## 本題關鍵學習
1. 我們很常遇到這種，以為需要轉資料結構的問題（像是 linked list 轉成 array、tree 轉成 graph），但通常都不需要，因為會額外浪費空間複雜度，甚至可能讓題目變得更複雜。
2. 不要小看 max 這個函式，因為有了它，我們不必真的只能挑一條最佳路徑，而是可以從眾多最佳路徑中取最大的，以這題為例，不要一開始 Dry run 時，就想要從 20 這個節點下去判斷，而是必須照著演算法的思維去走，也就是從根節點開始，開始的時候，你要知道一件事情，就是如果待會子節點能傳送一個東西回來，我能不能幫助解題，如果有的話，就可以運用 Recursive 來解決。

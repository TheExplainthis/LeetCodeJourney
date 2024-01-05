# Reorder List

[題目連結](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## 題目描述
原文：

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.  

----

GPT 4 翻譯：

給定一個鏈表的頭節點，從鏈表末尾移除第 `n` 個節點並返回其頭節點。

----

Example 1

![Example 1](example1.jpeg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

Example 2
```
Input: head = [1], n = 1
Output: []
```

Example 3
```
Input: head = [1,2], n = 1
Output: [1]
```

Constraints:

* The number of nodes in the list is `sz`.
* `1 <= sz <= 30`
* `0 <= Node.val <= 100`
* `1 <= n <= sz`

## 思路

直觀的做法是：  
1. 先數總鏈表長度是多少 -> O(N)  
2. 第二次再掃一次，到尾巴數來第 k + 1 個節點，移除尾巴數來第 k 個節點。  
這樣算起來時間複雜度 O(N)，空間複雜度 O(1)，感覺可行！

有沒有更好的做法？  
1. 上面的問題在於，做了掃兩遍鏈表這個動作，能不能改成 one-pass 呢？  
方法是有的：如果能用快慢指標，兩個指標距離為 k，那 fast 到尾巴的時候，剛好 slow 會在尾巴數來第 k + 1 個節點，就可以直接移除尾巴數來第 k 個節點。

**方法: One Pass**

* 步驟
    1. 先初始化 `slow` 和 `fast` 指標。
    2. `fast` 先往前走 `k` 步，`slow` 停留在原地不動。
    3. `slow` 和 `fast` 同時往前走，直到 `fast` 在最後一個節點。
    4. 移除 `slow.next`。

* 複雜度
    * 時間複雜度: O(N) # one pass
    * 空間複雜度: O(1)

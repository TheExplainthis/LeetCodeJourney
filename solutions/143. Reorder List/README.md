# Reorder List

[題目連結](https://leetcode.com/problems/reorder-list/)

## 題目描述
原文：

You are given the head of a singly linked-list. The list can be represented as:

`L0 → L1 → … → Ln - 1 → Ln`
*Reorder the list to be on the following form*:

`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


  

----

GPT 4 翻譯：

你獲得了一個單鏈表的頭節點。該鏈表可以表示為：

`L0 → L1 → … → Ln - 1 → Ln`
重新排列這個鏈表，使其變成以下形式：

`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`
你不能修改鏈表節點中的值。只能更改節點本身。

----

Example 1

![Example 1](example1.jpeg)

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

Example 2

![Example 2](example2.jpeg)

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```


Constraints:

* The number of nodes in the list is in the range `[1, 5 * 10^4]`.
* `1 <= Node.val <= 1000`

## 思路

這題應該蠻直觀的，就是像辦法把他切一半，後半段反轉之後和前半段合在一起，而上面說的三件事，我們前面幾題剛好都有做過。

* 方法：
    1. 找中心點：利用快慢指標找到正中央的節點。 -> O(N)
    2. 反轉指標：如 [206. Reverse Linked List](../206.%20Reverse%20Linked%20List/) 題一樣，利用三個指標反轉鏈表。 -> O(N)  
    3. 合併：如 [21. Merge Two Sorted Lists](../21.%20Merge%20Two%20Sorted%20Lists/) 題一樣，用兩個指標去把兩個鏈表串在一起。 -> O(N/2 + N/2)  
    * 所以這題是一題實作題，問題本身不難。

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(1)

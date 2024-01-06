# Merge k Sorted Lists

[題目連結](https://leetcode.com/problems/merge-k-sorted-lists/description/)

## 題目描述
原文：

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

----

GPT 4 翻譯：

你有一個包含 `k` 個連結列表 `lists` 的陣列，每個連結列表都按升序排序。

*將所有連結列表合併成一個排序的連結列表並返回它。*

----

Example 1

![Example 1](example1.jpeg)

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

Example 2
```
Input: lists = []
Output: []
```

Example 3
```
Input: lists = [[]]
Output: []
```

Constraints:

* `k == lists.length`
* `0 <= k <= 10^4`
* `0 <= lists[i].length <= 500`
* `-10^4 <= lists[i][j] <= 10^4`
* `lists[i]` is sorted in **ascending order**.
* The sum of `lists[i].length` will not exceed `10^4`.


## 思路

這題是 [21. Merge Two Sorted Lists](../21.%20Merge%20Two%20Sorted%20Lists/) 的延伸題型，如果說 21 題需要 2 個指標，那麼這題應該就是要 `k` 個指標，想到這裡可能就卡住了，因為我們過去練習的所有題目中，沒有這種動態生成指標的狀況。所以可能會開始靠著天賦硬刻。但你剛剛看完以上的論述，不覺得似曾相識的感覺嗎？  

就像是第 [206. Reverse Linked List](../206.%20Reverse%20Linked%20List/) 題一樣，要反轉兩個節點會需要 3 個指標，那我要反轉 `k` 個節點該怎麼辦？當初有一個做法是，利用遞迴每一次反轉兩個節點再傳回上一層。  

所以這題感覺也可以用一樣的邏輯，要合併 `k` 個鏈表，那我們先將兩個陣列合併成一個，再等著跟其他人合併，直到結束。  

上面這樣做會有什麼問題嗎？想像中不會有問題，但實際上可能會需要調整，因為如果照上面的做法做，在某個狀況就會導致效率有點變差：  
```
Input: lists = [[1,2,3,4,5,....500],[1,3],[2,6],[3,5],[4,7],[1,10],[3,20]]
```
上面的狀況在於，有一個鏈表超級長，其他都超級短，所以先合併 (0, 1)，再合併 (0, 2)、再合併 (0, 3) ... 以此類推，那個超長的第 0 號位置的鏈表，就會一直需要從頭跑過，避免以上狀況，可能需要程式上做一點調整，動一點手腳，簡單的做法可能有：  
1️⃣ 兩兩合併完成後，丟到陣列的最後方。  
2️⃣ 前後兩個先合併，所以會從長度 16 -> 變成 8 -> .. -> 最後合併成 1 個。  

上面的兩個做法是類似的，其實這就是傳說中的 Divide and Conquer，有發現嗎？我先把長度 `k` 的陣列 Divide 成小的問題（長度為 2 的陣列），再來 Conquer (合併兩個鏈表)，最後再來 Merge。  

**方法: Divide and Conquer**

* 步驟
    1. Divide: 將陣列分成兩兩一組。
    2. Conquer: 兩兩鏈表做合併。
    3. Merge: 直到最後只剩一個鏈表為止。

* 複雜度
    * 時間複雜度: O(Nlogk), N 為鏈表長度, k 為陣列長度
        * O(N) 為兩兩鏈表合併的時間複雜度。
        * O(logk) 為總共需要做 logk 次的合併。
    * 空間複雜度: O(1)

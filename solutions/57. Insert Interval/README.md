# Insert Interval

[題目連結](https://leetcode.com/problems/insert-interval/description/)

## 題目描述
原文：
  
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion. 

----

GPT 4 翻譯：

你給定了一個非重疊區間數組 `intervals`，其中 `intervals[i] = [start_i, end_i]` 代表第 `i` 個區間的開始和結束，且 `intervals` 按 `start_i` 升序排序。你還給定了一個區間 `newInterval = [start, end]`，代表另一個區間的開始和結束。

將 `newInterval` 插入到 `intervals` 中，使得 `intervals` 仍按 `start_i` 升序排序，且 `intervals` 仍然沒有任何重疊的區間（必要時合併重疊的區間）。

返回插入後的 `intervals`。

----

Example 1
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```


Constraints:
* `0 <= intervals.length <= 10^4`
* `intervals[i].length == 2`
* `0 <= start_i <= end_i <= 10^5`
* `intervals` is sorted by `start_i` in **ascending** order.
* `newInterval.length == 2`
* `0 <= start <= end <= 10^5`


## 思路：

如果還沒做過 [56. Merge Intervals](../56.%20Merge%20Intervals/) 建議可以先去做，這題只差了一點點，插在原先就已經排序好了，今天要把新的區間插入並重新合併他。

最簡單的做法，就是用 O(N) 的時間，把新的區間放進去，在用 O(N) 的時間一一合併，這樣就和 56 題一樣了，但這樣做有什麼問題呢？就是當把新區間插入陣列時，首先陣列在操作插入時需要 O(N) 的時間，而且在不同程式語言下，要插入元素可能會造成不同的空間複雜度影響，可能會需要開一個新的陣列，並把舊的元素複製過去，導致空間複雜度上升。

比較好得作法是，其實 `newInterval` 不需要真的插入進去，而是那他跟原本的陣列不斷地比較，判斷他會影響、重疊的區間做處理即可。

複雜度：
- 時間複雜度：O(N)
- 空間複雜度：O(1)

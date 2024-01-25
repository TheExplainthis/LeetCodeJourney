# Find Median from Data Stream

[題目連結](https://leetcode.com/problems/find-median-from-data-stream/description/)

## 題目描述
原文：

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for `arr = [2,3,4]`, the median is `3`.
For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.
Implement the MedianFinder class:

* `MedianFinder()` initializes the `MedianFinder` object.
* `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
* `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

----

GPT 4 翻譯：

**中位數**是有序整數列表中的中間值。如果列表的大小是偶數，則沒有中間值，中位數是兩個中間值的平均值。

例如，對於 `arr = [2,3,4]`，中位數是 `3`。
例如，對於 `arr = [2,3]`，中位數是 `(2 + 3) / 2 = 2.5`。
實現 MedianFinder 類：

* `MedianFinder()` 初始化 `MedianFinder` 物件。
* `void addNum(int num)` 將數據流中的整數 `num` 添加到數據結構中。
* `double findMedian()` 返回到目前為止所有元素的中位數。答案在實際答案的 `10^-5` 範圍內將被接受。

----

Example 1:

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

```

Constraints:

* `-10^5 <= num <= 10^5`
* There will be at least one element in the data structure before calling `findMedian`.
* At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

## 思路

最簡單的思路是，先將數列做排序，再搜尋時如果是偶數，就回傳 `(nums[n//2] +  nums[n//2 + 1]) / 2`、奇數的話就回傳 `nums[n//2]`。  

上面這樣做的好處是搜尋時很快 O(1)，但是加入數字時很慢 O(N)。有沒有什麼辦法，可以讓兩個操作複雜度可以盡可能取得平衡？  

上面的問題出自於，要維持有序陣列造成的，所以要從這一方面下手：如何在不排序得狀況下，又可以維持順序？而且複雜度會比 O(N) 更低？A: 這題要自己想真的會有點難，答案是可以用 Heap 來處理。  

版本一：用一個 Heap  
* `addNum` 時，每一次加入數字後，維持 min Heap 的架構 -> O(logN)。
* `findMedian` 時，若是偶數，每一次找到第 `(N//2)` 以及 `(N//2 + 1)` 大的數相加除以二；若是奇數就找到第 `(N//2)` 大的數做回傳 -> O( 1 * (N//2)) = O(N)。  
雖然 `addNum` 時，時間複雜度降低了，但是導致 `findMedian` 的時間複雜度上升。  

版本二：用兩個 Heap  
為了解決版本一的問題，如果能用兩個 Heap ，他能夠一直維持的狀態是：  
1️⃣ 第一個 Heap 維持 > 中位數的右半段。  
2️⃣ 第二個 Heap 維持 < 中位數的左半段。  
所以 `addNum` 時可以持續保持 O(logN) 的時間複雜度，而 `findMedian` 時可以直接找第一個 Heap 第一個數字以及第二個 Heap 的的一個數字來做處理，就可以在 O(1) 的時間內處理完。  
舉例來說：如果今天 addNum 順序為：`1,2,3,4,5,6,7,8,9,10` 我們可以來看一下 Heap 的狀況：  
加入 1: `maxHeap = [1]`, `minHeap = []`  
加入 2: `maxHeap = [1]`, `minHeap = [2]`  
加入 3: `maxHeap = [2, 1]`, `minHeap = [3]`  
加入 4: `maxHeap = [2, 1]`, `minHeap = [3, 4]`  
加入 5: `maxHeap = [3, 1, 2]`, `minHeap = [4, 5]`  
加入 6: `maxHeap = [3, 1, 2]`, `minHeap = [4, 5, 6]`  
加入 7: `maxHeap = [4, 3, 2, 1]`, `minHeap = [5, 7, 6]`  
加入 8: `maxHeap = [4, 3, 2, 1]`, `minHeap = [5, 7, 6, 8]`  
加入 9: `maxHeap = [5, 4, 2, 1, 3]`, `minHeap = [6, 7, 9, 8]`  
加入 10: `maxHeap = [5, 4, 2, 1, 3]`, `minHeap = [6, 7, 9, 8, 10]`  
最後來看的時候，兩個 Heap 的第一個位置，就會是 Median 所在的地方。


**方法: 利用兩個 Heap**

* 步驟
  1. 初始化 maxHeap 和 minHeap
  2. `addNum`
     1. 判斷插入哪個堆：
        1. 如果新數字小於或等於最大堆的頂部元素（或者最大堆是空的），將其插入最大堆。
        2. 否則，將其插入最小堆。
     2. 重新平衡堆：
        1. 如果兩個堆的大小差距超過 1，進行調整：
           1. 如果最大堆的大小比最小堆大 2 或以上，將最大堆的頂部元素移動到最小堆。
           2. 反之，如果最小堆的大小比最大堆大，將最小堆的頂部元素移動到最大堆。
        2. 這確保了兩個堆的大小維持平衡，從而方便計算中位數。
  3. `findMedian`
     1. 確定中位數：
        1. 如果數據總數是偶數，則中位數是最大堆的頂部元素和最小堆的頂部元素的平均值。
        2. 如果數據總數是奇數，則中位數是元素較多的那個堆的頂部元素。

* 複雜度
  * `addNum`
    * 時間複雜度: O(logN)
    * 空間複雜度: O(N)
  * `findMedian`
    * 時間複雜度: O(1)
    * 空間複雜度: O(1)

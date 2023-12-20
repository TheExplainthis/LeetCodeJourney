# Longest Consecutive Sequence
[題目連結](https://leetcode.com/problems/longest-consecutive-sequence/)

## 題目描述
原文：

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


----

GPT 4 翻譯：

給定一個未排序的整數陣列 nums，返回最長連續元素序列的長度。

你必須編寫一個時間複雜度為 O(n) 的演算法。


----

Example 1
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

Example 2
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

Constraints:

* `0 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

## 思路

很直觀的做法，就是會先排序，再掃過一次陣列，去比較當前數字，和前一個數字，如果兩個數字差 1，則代表有連續去，用這樣的方式逐一去找出最長的連續數字，但是這樣做無法滿足條件，因為題目要求需要在 O(N) 的時間複雜度內完成，所以先排序可能是有問題的，但別忘記，可以嘗試用空間去換取時間，要至於要用什麼樣的空間去做呢？


**方法 1: 排序**

* 步驟
    1. 先將 nums 做排序。
    2. 掃過一次陣列，判斷前後數字是否差 1，逐一檢查找出最長的連續數字。

* 複雜度
    * 時間複雜度: O(NlogN)
    * 空間複雜度: O(1)

**方法 2: Set**

* 步驟
    1. 先將 nums 放入「記憶區」。
    2. 掃過一次陣列，判斷當前數字 - 1 是否存在於「記憶區」。

* 記憶區的選擇
    * List: 不適合，List 查找時需要 O(N) 的時間。
    * Stack: 不適合，無法快速查找，需要 O(N) 的時間。
    * Hashmap: 適合，但只會用到 key 值，value 值用不太到。
    * Set: 最適合，因為只要判斷 key 是否存在，也僅需要 O(1) 的時間。

* 掃過要怎麼掃？
    * For Loop/While: 適合。
    * Sliding Window: 適合，用這樣的方式在看時間複雜度時，會更直觀。

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)

## Follow Up
1. 如果字串中數字有重複，是否會影響程式碼的正確性？

在 Approach 2 中，我們首先將數字存儲在 Set 中，這自然地去除了重複元素。因此，演算法在處理重複元素時仍然有效，無需修改。
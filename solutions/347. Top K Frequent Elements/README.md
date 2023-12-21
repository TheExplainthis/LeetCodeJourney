# Top K Frequent Elements
[題目連結](https://leetcode.com/problems/top-k-frequent-elements)

## 題目描述
原文：

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

----

GPT 4 翻譯：

給定一個整數陣列 nums 和一個整數 k，返回出現頻率最高的 k 個元素。你可以以任何順序返回答案。

----

Example 1
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2
```
Input: nums = [1], k = 1
Output: [1]
```

Constraints:

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `k` is in the range `[1, the number of unique elements in the array]`.
* It is **guaranteed** that the answer is **unique**.

## 思路

這題用人類的判斷方法很直觀，就是掃過一遍後，將每個數字出現的次數記住，然後再從出現次數最高排序到最低，然後挑選出現頻率前 K 大的數字。你也是這樣想的嗎？

基本上這樣想沒什麼問題，不果當你看到「從出現次數最高『排序』到最低」，就會知道這題應該就在考這個了，要怎麼聰明的挑到出現頻次前 K 大的數字，因為如果真的要排序，那時間複雜度 O(NlogN) 是跑不掉的，有沒有一個辦法把 O(NlogN)
 降到 O(N) 呢？

回到我們之前練習的題目，可以知道，空間是有機會替換時間的，有沒有一個「記憶區」能夠加快這個搜尋呢？如果不能用額外的空間，那是否有聰明的辦法，找到答案呢？

**方法 1: 空間換取時間**

* 步驟
    1. 數字從左掃到右。
        ```
        nums = [1,1,1,2,2,3]
        for num in nums:
            ...
        ```
    2. 取出來的 num 存放到某一個「記憶區」，希望存進去後，後面要取用時，是可以依照大小順序的。

* 記憶區的選擇
    1. 用 HashMap？
        * 不適合，因為存放進去後，取用時沒辦法依照大小順序取出。
    2. 用 Counter？
        * 不適合，雖然有提供 most_common(k) 的函式，但其內部是透過排序做到的，光排序時間複雜度會是 O(NlogN)。
    2. 用 Heap？
        * 適合，Heap 在取出時，可以從最小、或最大的開始取，Heap 在製作時，可以用 HashMap 協助。

* 複雜度
    * 時間複雜度: O(Nlogk)，其中 N 表數字串長度、k 表前 k 大的數字，時間複雜度可以分成：
        1. 先將數字存到 Heap 中 --> O(N)
        2. 因為只需要前 k 個元素，因此僅需保持 k 個元素所建立的 Heap --> O(k * logk)，logk 表示每多新加一個元素進去時，進行 heap 操作 (push/pop) 所需要的時間。
        3. 剩下 N - k 個元素，都要做 logk 的操作 (push/pop) 時間 --> O((N - k)logk)
        * O(N + klogk + (N-k) logk) = O(Nlogk)
    * 空間複雜度: O(N + k)
        1. Hashmap：存入所有數字 O(N)。
        2. Heap: 僅需維持 k 個元素的 heap，O(k)。

**方法 2: Quickselect**

Quickselect 很常應用在找第 k 大或小的題目，他的操作和 Quicksort 很像，Quickselect 的核心概念是，想像一下如果我先從陣列中，隨機挑一個 (數字, 出現的頻次)，然後其他得數字跟他比對，頻次比他小的放左邊、頻次比他大的放右邊，重複的做下去，是不是就有機會可以把第 k 大或小的數字找出來。詳細的步驟如下：

1. 分割（Partition）：如你所述，從數列中隨機選擇一個元素（稱為「樞軸」pivot）。然後，根據其他元素與樞軸的比較結果，將數列分成兩部分。頻次比樞軸小的元素放在左邊，頻次比樞軸大的元素放在右邊。樞軸元素本身將被放置在最終位置，這是如果數列被完全排序時它所應該在的位置。

2. 選擇（Select）：在分割之後，樞軸元素的位置（讓我們稱它為 index）將告訴我們它是第幾大（或小）的元素。如果 index 恰好等於 k，那麼我們就找到了我們要找的元素，演算法結束。如果 index 大於 k，這意味著我們要找的元素位於左側的子數列中，我們將在左側子數列中繼續進行 Quickselect。反之，如果 index 小於 k，則目標元素在右側的子數列中，我們將在右側子數列中繼續進行 Quickselect。

3. 遞迴：重複上述過程，每次都在越來越小的子數列中進行，直到找到第 k 大（或小）的元素。

備註：Quickselect 也非常像是 Binary Search，可以一起比較。

* 步驟
    1. 利用迴圈將每個數字出現的次數用 HashMap 來儲存。
    2. 利用 Quickselect 找到前 k 大的數。

* 複雜度
    * 時間複雜度: O(N)
        * Quickselect 在最糟的狀況，會是 O(N^2)，和 Quicksort 一樣，不過平均來說只要 O(N)。
    * 空間複雜度: O(N)
        * HashMap 本身需要 O(N) 的時間。

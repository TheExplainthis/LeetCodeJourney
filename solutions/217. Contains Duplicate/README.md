# 217. Contains Duplicate

[題目連結](https://leetcode.com/problems/contains-duplicate/)

## 題目描述
原文：

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

----

GPT 4 翻譯：

給定一個整數陣列 nums，如果陣列中任何值至少出現兩次則返回 true，如果每個元素都是獨一無二的則返回 false。

----

Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```

Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```

Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```


Constraints:

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

## 思路

這題如果有做過 [(E) 1. Two Sum](../1.%20Two%20Sum/) 那應該是輕鬆解，簡單的思維是：如果陣列從頭到尾掃一遍，要知道有沒有重複的，就代表要有一個記憶區，「把過去的數字存起來，然後去判斷當下的數字過去有存在嗎？」而希望判斷存不存在這件事情，時間複雜度可以在 O(1) ，所以選擇用 Set 是最佳的。

有沒有可能把空間複雜度壓到 O(1) ？是可以的，不過和過去說的一樣，空間和時間是交換出來的，如果壓低空間複雜度，代表時間複雜度會上升，簡單的方法是將陣列先排序，在掃一遍就可以知道答案了，這樣時間複雜度會來到 O(NlogN)。


**方法 1: Set**

* 步驟
    1. 掃過陣列，邊掃邊把數字存在 Set 中，只要 Set 存在，就代表重複了。

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)


**方法 2: Set**

* 步驟
    1. 先將陣列做排序。
    2. 在將陣列從頭掃到尾，判斷 nums[i] 是否等於 nums[i + 1] （小心 i 超出陣列長度）。

* 複雜度
    * 時間複雜度: O(NlogN)
    * 空間複雜度: O(1)


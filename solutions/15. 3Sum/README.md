# 3Sum
[題目連結](https://leetcode.com/problems/3sum/)

## 題目描述
原文：

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

----

GPT 4 翻譯：

給定一個整數數組 nums，返回所有這樣的三元組 `[nums[i], nums[j], nums[k]]`，滿足 `i != j`, `i != k`, 且 `j != k`，以及 `nums[i] + nums[j] + nums[k] == 0`。

請注意，解決方案集合中不能包含重複的三元組。

----

Example 1

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

Example 2
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

Example 3

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

Constraints:

* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

## 思路

這題是 [1. Two Sum](../1.%20Two%20Sum/) 的延伸題型，很直觀的做法是，先用 For Loop 掃過數字串，掃到第 1 個數字的時候，把第 2 ~ 最後一個數字做 Two Sum；掃到第 2 個數字的時候，把第 3 ~ 最後一個數字做 Two Sum，以此類推。


**方法 1: For Loop + Two Sum(HashMap) + Set**

* 步驟
    1. 掃過一次陣列，邊掃的時候把 2 ~ n 的數字做 Two Sum
        ```python
        for i, firstNum in enumerate(nums):
            # twoSum(nums[i+1:], -firstName)

        ```
    2. 重複的問題，利用 Set 來處理

* 複雜度
    * 時間複雜度: O(N^2)
    * 空間複雜度: O(N)

**方法 2: Sort + Two Pointer**

* 步驟
    1. 先將陣列做排序
    2. 用一個 For Loop 搭配 Two Pointer 如下：
        ```python
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                ...
        ```
    3. 需要處理重複的部分，重複的部分可以觀察一下何時會重複：
        - 情況一： 
            ```python
            nums = [-1,-1,0,1]
            # i = 0 時，內圈找到 [0, 1]
            # i = 1 時，內圈找到 [0, 1]
            ```
            所以外圈需要多加一個限制是：
            ```python
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ```
        - 情況二：
            ```python
            nums = [-1,0,1,1]
            # i = 0 時，內圈找到 [0, 1] 和 [0, 1]
            ```
            內圈也需要判斷，right 需要判斷是否已經有重複的數字了，如下
            ```python
            while right > 0 and nums[right] == nums[right+1]:
                right -= 1
            ```

* 複雜度
    * 時間複雜度: O(N^2)
    * 空間複雜度: O(logN) ~ O(N) # 看選用哪一個排序方法

# Two Sum

## 題目描述
原文：

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

----

GPT 4 翻譯：

給定一個整數陣列 nums 和一個整數 target，返回兩個數字的索引，使得它們相加之和等於 target。

你可以假設每個輸入都恰好只有一個解決方案，並且你不能重複使用相同的元素。

你可以以任何順序返回答案。

----

Example 1
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
Example 3
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## 解題思路

首先要思考的是，是否需要掃描整個陣列才能找到答案。如果答案是肯定的，則至少需要一個 For Loop 來解決，這意味著時間複雜度至少是 O(N)。

其次，我們需要考慮是否能在單次掃描中直接找到答案。假設你在腦海中模擬這個過程，你會發現，在 For Loop 的過程中，你會開始忘記之前掃過的數字。例如，在處理上面的示例時，當你到達數字 7，你需要記得之前已經出現過數字 2。

因此，我們需要一種方法來「記住」之前掃過的數字。有兩種主要方法：

* 方法 A
    * 使用兩個指標，一個固定在某個數字上，另一個掃描剩餘的數字。這需要兩個嵌套的 For Loop，時間複雜度為 O(N^2)，但空間複雜度為 O(1)。

* 方法 B
    * 使用一種資料結構來記住過去的數字。每掃過一個數字，就記下來，以便之後可以查找是否有數字與當前數字組合能匹配 target。建議使用 HashMap，因為它可以同時記錄數字及其索引。這樣做的時間複雜度是 O(N)，但空間複雜度提高到 O(N)。

## Follow Up：有序陣列的情況
如果初始陣列 nums 是有序的，該如何解決？

考慮點
* 掃描需求：依然需要掃過一遍才能知道答案所在。
* 遺忘問題：在有序陣列中，不會有遺忘問題。我們可以使用兩個指標（前後型 Two Pointer）來解決。當兩指標相加之和大於 target 時，右指標向左移動，反之則左指標右移。

```
def twoSumSorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []    
```
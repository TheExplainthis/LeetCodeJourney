# Find Minimum in Rotated Sorted Array
[題目連結](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## 題目描述
原文：

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

* `[4,5,6,7,0,1,2]` if it was rotated `4` times.
* `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n) time.`


----

GPT 4 翻譯：

假設一個長度為 `n` 且按升序排序的陣列被**旋轉**了 `1` 到 `n` 次。例如，陣列 `nums = [0,1,2,4,5,6,7]` 可能變成：

* `[4,5,6,7,0,1,2]` 如果它被旋轉了 `4` 次。
* `[0,1,2,4,5,6,7]` 如果它被旋轉了 `7` 次。

注意，對陣列 `[a[0], a[1], a[2], ..., a[n-1]]` 旋轉 `1` 次的結果是陣列 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`。

給定一個由**唯一**元素組成的已排序且旋轉過的陣列 `nums`，返回*這個陣列的最小元素*。

你必須寫出一個在 `O(log n)` 時間內運行的演算法。

----

Example 1

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

Example 2
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

Example 3

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
```

Constraints:

* `n == nums.length`
* `1 <= n <= 5000`
* `-5000 <= nums[i] <= 5000`
* All the integers of `nums` are **unique**.
* `nums` is sorted and rotated between `1` and `n` times.



## 思路

這題看似簡單，掃過一次陣列就可以知道最小值在哪裡，但是題目有規定，要利用 O(logN) 的時間複雜度解決，所以這題必須要重新想這題，但題目也有線索，就是 O(logN) + 找最小值 + 已排序 = 這有很高的機率可以用 Binary Search。  

但是 Binary Search 要怎麼找呢？這邊我們先列出 1 2 3 4 5，然後讓旋轉，選轉後切一半，觀察一下狀況：  
第一種： 1 2 **3** 4 5，前半：(正序)；後半：(正序)，最小值在最左邊  
第二種： 2 3 **4** 5 1，前半：(正序)；後半：(亂序)，最小值在右邊  
第三種： 3 4 **5** 1 2，前半：(正序)；後半：(亂序)，最小值在右邊  
第四種： 4 5 **1** 2 3，前半：(亂序)；後半：(正序)，最小值在右邊  
第五種： 5 1 **2** 3 4，前半：(亂序)；後半：(正序)，最小值在左邊  

整理一下：
if (前半正序 && 後半正序): right = mid - 1
elif (前半正序): left = mid
else: right = mid - 1



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

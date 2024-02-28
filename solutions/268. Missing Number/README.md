# Missing Number

[題目連結](https://leetcode.com/problems/missing-number/description/)

## 題目描述
原文：
  
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*
 
----

GPT 4 翻譯：

給定一個包含 `n` 個不同數字的數組 `nums`，這些數字在範圍[0, n]內，返回*範圍內唯一缺失的數字*。

----

Example 1
```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

Example 2
```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

Example 3
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

Constraints:
* `n == nums.length`
* `1 <= n <= 10^4`
* `0 <= nums[i] <= n`
* All the numbers of `nums` are **unique**.


## 思路：

最簡單的做法，就是排序他，就可以知道哪一個數字有缺，但排序所需要的時間複雜度需要 O(NlogN)；第二個方法可以是利用 Set，把每一個數字丟到 Set 中，就可以知道哪一個數字有缺，這樣的問題在於，空間複雜度會需要到 O(N)。

這題可以直接用 bit 的做法來處理，因為自己和自己互斥或會 = 0，意思是：

```
5 ^ 5 = 0
3 ^ 3 = 0
...
```

因為陣列範圍在 `[0, n]` 之間，因此如果能把存在的數字做互斥或，則可以變為 0 ，剩下來的數字就是我們要的，可以觀察以下狀況：

```
index = 0, 1, 2, 3
value = 1, 3, 0, 4
```

missing = 4 ^ (0 ^ 1) ^ (1 ^ 3) ^ (2 ^ 0) ^ (3 ^ 4)
又會等於 4 ^ 0 ^ 1 ^ 1 ^ 3 ^ 2 ^ 0 ^ 3 ^ 4
在重新整理一下： 4 ^ 4 ^ 0 ^ 0 ^ 1 ^ 1 ^ 3 ^ 3 ^ 2 
最後會剩下：0 ^ 0 ^ 0 ^ 0 ^ 2

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)

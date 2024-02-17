# Maximum Subarray

[題目連結](https://leetcode.com/problems/maximum-subarray/description/)

## 題目描述
原文：
  
Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

----

GPT 4 翻譯：

給定一個整數數組 `nums`，找出具有最大和的子數組，並返回*其和*。

----

Example 1
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

Example 2
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

Example 3
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```
Constraints:
* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`



## 思路：

貪婪法則（Greedy Algorithm）是一種在每一步選擇中都採取在當前狀態下最好或最優（即最有利）的選擇，從而希望導致結果是全局最好或最優的算法策略。貪婪算法解決問題的過程中，作出的選擇不能改變，也就是說，每步選擇一旦做出，就不再重新考慮了。貪婪法則能夠應用的條件主要包括兩個重要概念：貪婪選擇性質和最優子結構。

1. 貪婪選擇性質：算法能夠作出局部最優選擇，在這個選擇被做出之後，這個選擇就將其餘的問題實例減少為一個新的問題。貪婪選擇性質保證局部最優選擇能夠導致全局的最優解決方案。這意味著，作出的貪婪選擇在過程中不需要後悔或重新考慮。

2. 最優子結構：問題的最優解包含了其子問題的最優解，這些子問題可以獨立於原問題獨立求解。最優子結構意味著問題可以通過其子問題的最優解組合得到全局最優解。

而以這題為例：  
1. 貪婪選擇性質: 對於每一個元素，要麼將當前元素加入到當前子數組的和中（如果它能使得和增加），要麼從當前元素開始一個新的子陣列。
2. 最優子結構: 對於任何一個位置 `i`，其最大子數組和要麼是包含 `nums[i]` 的最大子數組和，要麼是不包含 `nums[i]`（即在i之前某處結束）的最大子數組和。

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)

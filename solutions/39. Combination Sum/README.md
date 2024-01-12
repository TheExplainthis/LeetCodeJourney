# Combination Sum

[題目連結](https://leetcode.com/problems/combination-sum/description/)

## 題目描述
原文：

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of candidates where the chosen numbers sum to target.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.


----

GPT 4 翻譯：

給定一個**不重複**整數數組 `candidates` 和一個目標整數 `target`，返回*所有**唯一組合**的列表，這些組合中選擇的數字之和為 `target`。* 你可以以**任何順序**返回這些組合。

可以從 `candidates` 中**無限次**選擇**相同**的數字。如果至少一個選擇數字的
頻率
不同，則兩個組合是唯一的。

測試案例生成的方式，確保對於給定的輸入，加總為 `target` 的唯一組合數量少於 `150` 個組合。

----

Example 1
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

Example 2
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

Example 3
```
Input: candidates = [2], target = 1
Output: []
```

Constraints:

* `1 <= candidates.length <= 30`
* `2 <= candidates[i] <= 40`
* All elements of `candidates` are **distinct**.
* `1 <= target <= 40`


## 思路

這題有看到一個關鍵字，就是 **Combination** ，這題很適合使用 Backtracking 的策略，每一個數字變成選或不選的問題，而且可以重複選。對於這個問題，我們從 candidates 數組中選擇數字，並逐一嘗試添加到當前組合中，然後檢查這些組合的和是否等於目標值 target。


**方法: Backtracking**

* 步驟
  1. 初始化：創建一個空列表來存儲當前的組合（path）和一個結果列表來存儲所有合法的組合（results）。
  2. 遞歸函數：創建一個遞歸函數，用於遍歷 candidates，並將當前的數字添加到 path 中。
  3. 檢查和：在每次遞歸調用中，檢查 path 中數字的總和。
     1. 如果總和等於 target，將 path 的一個副本添加到 results 中。
     2. 如果總和大於 target，則返回上一步（回溯）。
  4. 遞歸和回溯：對每個數字，遞歸地呼叫函數，每次都加上當前數字。在遞歸返回後，從 path 中移除最後一個數字（回溯）。
  5. 返回結果：當遍歷完所有可能性後，返回 results。

        
* 複雜度
    * 時間複雜度: O(N^M)，其中 N 是 candidates 數組的長度，M 是 target 和最小候選數字之間的最大可能組合數。因為每個元素可以被無限次選擇，所以在最壞情況下，算法需要遍歷所有可能的組合。
    * 空間複雜度: O(M)，這是遞迴 Stack 的最大深度，也就是達到目標和所需的最大步數。在最壞的情況下，這等於 target 數除以最小候選數字。

# Jump Game

[題目連結](https://leetcode.com/problems/jump-game/description/)

## 題目描述
原文：
  
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

----

GPT 4 翻譯：

給定一個整數陣列 `nums`。你最初位於陣列的**第一個索引處**，且陣列中的每個元素代表你在該位置的最大跳躍長度。

如果你能到達最後一個索引，則返回 `true`；否則返回 `false`。

----

Example 1
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```


Constraints:
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 10^5`



## 思路：

這個問題適合使用貪婪法則（Greedy Algorithm），因為在每一步跳躍時，我們可以根據當前能達到的最遠距離來做出最優選擇，從而決定下一步的跳躍。這個方法適合因為：

1. 局部最優解導向全局最優解： 貪婪法則的核心在於從當前位置做出能使我們朝目標（達到最後一個索引）前進最遠的選擇。透過在每一步都選擇可以跳得最遠的位置，我們可以保證這種局部的最優決策最終將導致全局的最優解。

2. 無需回溯： 在這個問題中，一旦我們選擇了從某一位置跳躍到下一個位置，就沒有必要回頭再考慮其他的跳躍選擇，因為我們總是選擇能跳得最遠的選項。這種性質使得貪婪法則非常適合，因為我們不需要考慮所有可能的跳躍路徑，從而節省了計算資源。

3. 簡單且高效： 使用貪婪法則，我們可以通過一次遍歷（O(n)時間複雜度）來解決這個問題，無需複雜的動態規劃或回溯算法。在每次遍歷過程中，更新能達到的最遠距離，如果在某一步，這個最遠距離大於等於最後一個索引，則意味著我們可以到達最後一個索引。


* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)

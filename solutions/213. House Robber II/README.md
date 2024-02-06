# House Robber II

[題目連結](https://leetcode.com/problems/house-robber-ii/description/)

## 題目描述
原文：
  
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

----

GPT 4 翻譯：

你是一位專業的強盜，計畫著沿街搶劫房屋。每間房屋都藏有一定數量的金錢。這些房屋在這個地方是以圓圈的形式排列的，這意味著第一間房屋是最後一間房屋的鄰居。同時，相鄰的房屋有連接的安全系統，如果同一晚上有兩間相鄰的房屋被闖入，系統會自動聯繫警察。

給定一個整數陣列 nums，代表每間房屋的金錢數量，返回今晚你能在不引起警察注意的情況下搶劫的最大金額。

----

Example 1
```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

Example 2
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

Example 3
```
Input: nums = [1,2,3]
Output: 3
```

Constraints:

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 1000`

## 思路:

這題和上一題 [198. House Robber](../198.%20House%20Robber/) 相比，多了一個限制條件，是將頭和尾的兩間房子視為相鄰。因此上一題的做法需要修改。

如果 `nums = [6, 7, 1, 5, 3, 4, 2]  `
情況1： 則如果從 `6` 開始考慮要不要偷，則最後的 `2` 就會不能當作選擇。  
情況2： 而如果從 `7` 開始考慮要不要偷，則最後的 `2` 就可以當作選擇。  
  
有些比較謹慎的同學，可能就會想說，可是 情況 1 雖然從 `6` 開始判斷要不要偷，但未必真的從 `6` 開始啊!以這題為例，第 1 間 `7` 的價值明顯比較高（所以第 0 間不偷），這樣的話最後一個 `2` 就可以偷了不是嗎？  
  
非常好！這位同學的自白已經說完了，他提到的狀況剛好是 情況 2 會考慮到的，所以不用擔心會有問題。
    
所以答案其實很簡單，就是 198 題做兩次，第一次是計算從[第 0 間] 到 [第 n - 1 間]，第二次是計算[第 1 間] 到 [第 n 間]，兩個取大的那個就是答案。


## 方法: DP 做兩次

```
def 198_solution(nums):
    ...

return max(198_solution(nums[:-1]), 198_solution(nums[1:]))
```

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)

# House Robber

[題目連結](https://leetcode.com/problems/house-robber/description/)

## 題目描述
原文：
  
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

  

----

GPT 4 翻譯：

你是一位專業的強盜，計畫著在一條街上搶劫房屋。每間房屋都藏有一定數量的金錢，唯一阻止你搶劫它們的限制是相鄰的房屋有連接的安全系統，如果同一晚上有兩間相鄰的房屋被闖入，系統會自動聯繫警察。

給定一個整數陣列 nums，代表每間房屋的金錢數量，返回今晚你能在不引起警察注意的情況下搶劫的最大金額。

----

Example 1
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

Example 2
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

```

Constraints:

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 400`

## 思路:

首先判斷這題適合用什麼解法時，可以先分析一下題目，首先這題當中每一個房子有搶、和不搶兩個選項，所以可以發展出一個決策樹，可以在這個決策樹上做 Backtracking，找到所有的可能，最後在找出金額最高的狀況。而因為可以做 Backtracking、而且只要求一個數值，所以可以透過 Memorization 的方式來加速。


## 方法 A: Recursive + Memorization

利用 Recursive 的思維，可以知道先從第一個房子開始考慮，每一個房子有兩個選項，搶、不搶，如果搶了，那就獲得該房子的金額；如果不搶，那就跳過直接看下一間房子的狀況。如下：

```
memo = {}
def recursive(i):
    if not valid(i): return 0
    if i in memo: return memo[i]
    rob = nums[i] + recursive(i + 2)
    not_rob = recursive(i + 1)
    memo[i] = max(rob, not_rob)
    return memo[i]
recursive(0)
```

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(N)

## 方法 B: Dynamic Programming

方法 A 的做法，剛好可以用 Iterative 的方式來做，轉移方程式為：
```
dp[0] = nums[0]
dp[1] = max(dp[0], 0 + nums[1])
...
dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])
```

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(N)

## 方法 B: Dynamic Programming + Optimize

上一題 [70. Climbing Stairs](../70.%20Climbing%20Stairs/) 可以知道，其實我們只需要儲存兩個狀態的值就好，不需要真的開一個陣列儲存所有狀態。

```
first = nums[0]
second = max(first, nums[1])
third = max(second, first + nums[i])
```

* 複雜度：
  * 時間複雜度：O(N)
  * 空間複雜度：O(1)
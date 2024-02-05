# Climbing Stairs
[題目連結](https://leetcode.com/problems/climbing-stairs/)

## 題目描述
原文：
  
You are climbing a staircase. It takes n steps to reach the top.  
  
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?  

----

GPT 4 翻譯：

您正在爬樓梯。要到達頂部需要 n 個階梯步。  

每次您可以爬 1 或 2 個階梯步。您可以用多少種不同的方式爬到頂部？  

----

Example 1
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Example 2
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Constraints:

* `1 <= n <= 45`

## 思路 1: Recursive (TLE)

這題可以用遞迴的方式來思考，如果要計算踩到第 n 階的方法數，則代表可以計算踩到第 n - 1 的方法數 + 第 n - 2 的方法數。

```
def dp(n):
    return dp(n - 1) + dp(n - 2)
```

* 複雜度
    * 時間複雜度: O(2^n)
    * 空間複雜度: O(n)

## 思路 2: Recursive + Memoization

因為每一次遞迴都有大量重複的運算，所以可以用一個 hashmap 把計算過的數值都記錄下來，這樣就可以加快運算。

```
hashmap = {}
def dp(n):
    if n in hashmap:
        return hashmap[n]
    return dp(n - 1) + dp(n - 2)
```

* 複雜度
    * 時間複雜度: O(n)
    * 空間複雜度: O(n)

## 思路 3: Dynamic Programming

DP 通常會比方法二再多做一件事情，就是找出轉移方程式，而這題的轉移方程為：  
```
dp = [-1] * (n + 1)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[n] = dp[n - 1] + dp[n - 2]
```

* 複雜度
    * 時間複雜度: O(n)
    * 空間複雜度: O(n)

## 思路 4: Dynamic Programming (Optimize)

因為 dp 每一次只會管理兩個狀態，所以只需要用兩個變數儲存就好了，毋需真的用一個陣列儲存。

```
first = 1
second = 2
for i in range(3, n + 1):
    third  = first + second
    first, second = second, third
```

* 複雜度
    * 時間複雜度: O(n)
    * 空間複雜度: O(1)

# 思路 5: Math (Fibonacci Formula)

剛好這題就是在考 Fibonacci ，可以直接套用數學公式。

```
sqrt5 = math.sqrt(5)
phi = (1 + sqrt5) / 2
psi = (1 - sqrt5) / 2
res = int((phi**(n + 1) - psi**(n + 1)) / sqrt5)
```

* 複雜度
    * 時間複雜度: O(1) 
    * 空間複雜度: O(1)
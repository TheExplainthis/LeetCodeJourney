# Best Time to Buy and Sell Stock  
[題目連結](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## 題目描述
原文：

You are given an array prices where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

----

GPT 4 翻譯：

你有一個數組 `prices`，其中 `prices[i]` 是第 `i` 天給定股票的價格。

你希望通過選擇**一天**買入一股並在**未來的某一天**賣出該股票來最大化你的利潤。

返回你能從這筆交易中獲得的最大利潤。如果你無法獲得任何利潤，則返回 `0`。

----

Example 1
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

Example 2
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

Constraints:

* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`

## 思路

直觀的思維：盡可能地找低點買入、盡可能的在買入後找一個最高點賣掉。但要以演算法的思維來想，計算機沒有上帝視角，他沒辦法第一時間就知道低點以及高點在哪裡，他能做的事情是：「盡可能把所有低買高賣的利潤位記住，最後再取 Max」。

有了以上的心理準備後，暴力解的方法就是：找到所有的 Pair （e.g. (位置 0 買, 位置 1 賣), (位置 0 買, 位置 2 賣), ...），最後取 Max，但這樣的做法會太慢，而且其實有「大量不必要的計算」，像是「若不小心買在高點，那人類就會知道，沒救了，後面不用計算了」！所以能加快的做法就是，在找 Pair 的時候，也不斷更新可能的低點，避免大量不必要的運算，而這樣的做法剛好就非常符合「Sliding Window」的做法。

很多人可能會知道這個 Sliding Window，但最困難的問題在於：「我怎麼知道這題要用 Sliding Window？」，所以經由這題，至少有線索是：    
1️⃣ 要利用這兩個點來計算時  
2️⃣ 透過不斷地更新這兩個點，可以加快運算  

**方法: Sliding Window**

* 步驟
    1. 初始化 `slow` 和 `fast` 指標
    2. `fast` 指標一次往後走一格，並且去紀錄 `prices['fast'] - prices['slow']` 的值。
    3. 最重要的一步來了：如果 `slow` 所在的值比 `fast` 所在的值還要大，那就要更新 `slow`，意思如下：
        ```python
        if prices['slow'] > prices['fast']:
            slow = fast
        ```
        表示後面有更低的低點，應該要選「更低的低點」，前面的就捨棄不看了！（備註：所以一路往下跌，不做交易就是最好的選擇。）

* 複雜度
    * 時間複雜度: O(N) # fast 將每一個數字掃過一次。
    * 空間複雜度: O(1)


---
## 延伸討論
1. Sliding Window 的關鍵在於 slow 和 fast 指標該如何移動，就跟 Two Pointer 的 left 和 right 指標一樣。  
2. 有沒有模板可以使用？ 網路上有提供兩種模板 ，但我不建議去使用，因為為了背模板，反而在看到新題目時會感到慌張。  
3. 爲什麼叫做 slow 和 fast？因為他和快慢型的 Two Pointer 有 87% 像。  
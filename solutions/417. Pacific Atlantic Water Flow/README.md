# Pacific Atlantic Water Flow

[題目連結](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

## 題目描述
原文：

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return *a **2D list** of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to *both* the Pacific and Atlantic oceans.*

----

GPT 4 翻譯：

有一個 `m x n` 的矩形島嶼，它與**太平洋**和**大西洋**相鄰。**太平洋**接觸島嶼的左側和頂部邊緣，而**大西洋**接觸島嶼的右側和底部邊緣。

該島嶼被劃分成一個方格網格。給定一個 `m x n` 的整數矩陣 `heights`，其中 `heights[r][c]` 代表坐標 `(r, c)` 處單元格的**海拔高度**。

該島嶼降雨量大，雨水可以流向北、南、東、西的鄰近單元格，如果鄰近單元格的高度**小於或等於**當前單元格的高度。任何與海洋相鄰的單元格中的水都可以流入海洋。

返回一個**二維列表**的網格坐標 `result`，其中 `result[i] = [ri, ci]` 表示雨水可以從單元格 `(ri, ci)` 流向**太平洋和大西洋**。

----

Example 1

![Example 1](example1.jpeg)
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

Example 2
```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```


Constraints:

* `m == heights.length`
* `n == heights[r].length`
* `1 <= m, n <= 200`
* `0 <= heights[r][c] <= 10^5`

## 思路

看到這種很人類思維的題目，就一定要小心避免自己很直觀的思維，像是說：「那就是找山脈呀，我從對角線開始看...」 之類的，因為題目可不是要叫你找山脈。  

用演算法的思維來想，我們現站在隨便一格 `(r, c)` ，要判斷他是不是比周遭的格子還要大，而且要不斷地地回下去，直到有格子碰到左上和右下才可以。  

首先幾個線索，BFS 應該是必須要做的，因為要遍歷過全部才能知道狀況；再來是，如果每個格子都去做 BFS，感覺一定會 TTL（超時），複雜度應該會落在 O(M * N * 4^max(M, N))，那有什麼辦法可以加快呢？  

首先會有幾種想法：  
✅ 如果 (r, c) 已經先前被確認可以流到左上、或右下了，那就不用再重新算了。
❓ 要用什麼方法來儲存這個資訊？
❓ 解決重複的問題，那適合使用 Dynamic Programming 嗎？

直觀來說，可能可以用一些 Hashmap 或者 Set 來做，因為他只要 O(1) 的時間就能夠搜尋到；可能也可以用 dynamic programming，因為可以從最靠上面的邊往下推、最靠左的邊往右邊推，效果應該相同。


**方法：DFS**

實際上要判斷流到左或上和流到右或下，需要用兩個記憶區來處理，因為什麼叫做能流到左或上，意思是左邊的數字比右邊小或者上面的數字比下面小，叫做可以留到左或上；相反的，留到右或下的意思是，右邊的數字要比左邊小或者下面的數字要比上面小。  

DFS 會是：  
```
dfs(row, col, 上一個數字):
    if (已經被流過 or 超出範圍 or 比上一個數字小): return
    (row, col)加入 visited
    for (dr, dc) in [其他四個方向]:
        dfs(row + dr, col + dc, heights[row][col])
```

所以第一次呼叫函示時需要分兩次來做：
1. 第一次（看左右）
    ```
    for i in range(m):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, n - 1, atlantic, heights[i][n - 1])
    ```
2. 第二次（看上下）
    ```
    for j in range(m):
        dfs(0, j, pacific, heights[0][j])
        dfs(m - 1, j, atlantic, heights[m - 1][j])
    ```
最後再去取交集，若某一個格子同時在 pacific 和 atlantic 都能被找到，代表可以流向這兩個地方。


**複雜度**
  * 時間複雜度：O(M * N)
  * 空間複雜度：O(M * N)
  * 備註：M 為長、 N 為寬

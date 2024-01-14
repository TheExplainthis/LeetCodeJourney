# Graph Valid Tree

[題目連結](https://leetcode.com/problems/graph-valid-tree/description/)

## 題目描述
原文：

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` *if the edges of the given graph make up a valid tree, and `false` otherwise.*

----

GPT 4 翻譯：

您有一個由 `0` 到 `n - 1` 標記的 `n` 個節點的圖。您被給予一個整數 n 和一個 `edges` 列表，其中 `edges[i] = [ai, bi]` 表示在圖中節點 `ai` 和 `bi` 之間有一條無向邊。

如果給定圖的邊構成一個有效的樹，則返回 `true`，否則返回 `false`。

----

Example 1

![Example 1](example1.jpeg)

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

Example 2

![Example 2](example2.jpeg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```


Constraints:

* `1 <= n <= 2000`
* `0 <= edges.length <= 5000`
* `edges[i].length == 2`
* `0 <= ai, bi < n`
* `ai != bi`
* There are no self-loops or repeated edges.

## 思路

如果要是有效的 Tree，會有幾個條件：  
1. N 個節點需要有 N-1 個邊
2. 不得有環路
3. 不得有兩棵樹以上

**方法: BFS**

* 步驟
  1. 檢查邊的數量：
     * 首先判斷邊的數量是否等於節點數減一 `len(edges) != (n - 1)` 。在一個有效的樹中，邊的數量總是等於節點數減一。如果不符合這個條件，則直接返回 `False`。 
  2. 建立圖的鄰接表：
     * 使用 `defaultdict(list)` 創建一個圖的鄰接表（`graph`）。遍歷每條邊，將邊的兩個節點加入對方的鄰接列表中。這樣可以快速找到任何節點的所有鄰居。
  3. 使用廣度優先搜索（BFS）遍歷圖：
     * 初始化一個訪問過的節點集合 `visited`，並將起始節點 `0` 加入其中。
     * 使用雙端隊列 `collections.deque` 作為 BFS 的隊列，並將起始節點 `0` 加入隊列。
     * 當隊列不為空時，從隊列中取出一個節點 `node`，遍歷該節點的所有鄰居。
     * 如果鄰居節點尚未被訪問，則將其加入訪問過的節點集合並加入隊列。這樣可以確保每個節點只被訪問一次。
  4. 檢查是否訪問了所有節點：
     * 最後，檢查訪問過的節點數量 `len(visited)` 是否等於總節點數 `n`。如果相等，則表示所有節點都被連通，且沒有多餘的邊造成環，因此構成了一個有效的樹；否則，返回 `False`。

        
* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)

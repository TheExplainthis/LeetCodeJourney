# Course Schedule

[題目連結](https://leetcode.com/problems/course-schedule/description/)

## 題目描述
原文：

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

* For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

----

GPT 4 翻譯：

你需要修總共 `numCourses` 個課程，這些課程從 `0` 到 `numCourses - 1` 標記。你會獲得一個數組 `prerequisites`，其中 `prerequisites[i] = [ai, bi]` 表示如果你想修課程 `ai`，你**必須**先修課程 `bi`。

* 例如，配對 `[0, 1]` 表示要修課程 `0`，你必須先修課程 `1`。

如果你能完成所有課程，則返回 `true`。否則，返回 `false`。


----

Example 1

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

Example 2

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```


Constraints:

* `1 <= numCourses <= 2000`
* `0 <= prerequisites.length <= 5000`
* `prerequisites[i].length == 2`
* `0 <= ai, bi < numCourses`
* All the pairs prerequisites[i] are **unique**.


## 思路

這題可以用 Graph 的思維來想，例如輸入給 `[0, 1]` 代表`節點 1 -> 節點 0`，表示要先有`節點 1 `就能夠遍歷到`節點 0`，而如果要完成所有課程，需要滿足兩個條件：  
1. 整個 Graph 不能有 Cycle，如範例二。  
2. 所有課程都要被訪問到。  


**方法 1: Topological Sort**

不要被 Topological sort 這個名字嚇到了，覺得好像是一個很難的演算法，想說我沒背到該怎麼辦，其實做法很簡單，幾個步驟：  
1. 先將輸入改成 Graph 的形式，建議可以使用 Hashmap 來做，為什麼？因為比較簡單。
2. 要針對這個 Graph 做 BFS，而做的時候是有順序的。
   1. 要先從 indegree = 0 的節點開始做。
   2. 每一次遍歷完的節點，他的子節點 indegree 要減 1。
   3. 不斷地從 indegree = 0 的節點中挑一個出來做。
3. 若最後已經拜訪過的節點 != numCourses 則回傳 False。

* 複雜度
  * 時間複雜度: O(M + N)
    * 初始化 Graph：O(M)
    * 遍歷所有節點：O(N)
  * 空間複雜度: O(M + N)
    * 儲存所有的邊：O(M)
    * 儲存所有節點的 indegree 值：O(N)
    * Queue 最大值：O(N)
  * N 為所有課程數量，M 為 `prerequisites` 的長度。

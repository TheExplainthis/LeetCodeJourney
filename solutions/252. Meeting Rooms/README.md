# Meeting Rooms

[題目連結](https://leetcode.com/problems/meeting-rooms/description/)

## 題目描述
原文：
  
Given an array of meeting time `intervals` where `intervals[i] = [start_i, end_i]`, determine if a person could attend all meetings.

----

GPT 4 翻譯：

給定一個會議時間的陣列 `intervals`，其中 `intervals[i] = [start_i, end_i]`，判斷一個人是否能參加所有會議。

----

Example 1
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

Example 2
```
Input: intervals = [[7,10],[2,4]]
Output: true
```

Constraints:
* `0 <= intervals.length <= 10^4`
* `intervals[i].length == 2`
* `0 <= start_i < end_i <= 10^6`


## 思路：

這題是 56 題的簡單版，不需要合併，只需要判斷有沒有重疊即可，因此只需要將區間排序一遍，再用一個迴圈去兩兩比較，就可以知道是不是有重疊了。

複雜度：
- 時間複雜度：O(NlogN) 
- 空間複雜度：O(logN)

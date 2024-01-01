# Search in Rotated Sorted Array
[題目連結](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## 題目描述
原文：

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

----

GPT 4 翻譯：

存在一個按升序排列的整數陣列 `nums`（具有**不重複**的值）。

在傳遞給您的函數之前，`nums` **可能會在未知的軸心索引 `k` 上旋轉**（`1 <= k < nums.length`），使得結果陣列變為 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（**從0開始索引**）。例如，`[0,1,2,4,5,6,7]` 可能在軸心索引 `3` 處旋轉並變成 `[4,5,6,7,0,1,2]`。

給定**可能旋轉後**的陣列 `nums` 和一個整數 `target`，如果 `target` 在 `nums` 中，則返回 `target` 的索引；如果不在 `nums` 中，則返回 `-1`。

您必須寫出一個具有 `O(log n)` 運行時間複雜度的演算法。

----

Example 1

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Example 2
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

Example 3

```
Input: nums = [1], target = 0
Output: -1
```

Constraints:

* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i] <= 10^4`
* All values of `nums` are **unique**.
* `nums` is an ascending array that is possibly rotated.
* `-10^4 <= target <= 10^4`


## 思路

這題和 [153. Find Minimum in Rotated Sorted Array](../153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/) 很像，所以可以持續用 153 題的思路來做延伸，最簡單的做法，就是利用 153 題找到最小值，再把陣列切分成一半，左邊用 Binary Search 去找 `target`、右邊用 Binary Search 去找 `target`，都沒找到就返回 `-1`。

有沒有更快的做法呢？因為感覺先找最小值的過程中，答案應該就要能呼之欲出，但真的是這樣嗎？可能需要嘗試看看：  
Input: `nums = [4,5,6,7,0,1,2]`  

當 `target = 4`  
第一輪搜尋： 4 5 6 **7** 0 1 2，切一半後來看， `target` 可能在哪裡？在左邊，因為他介於 `left <= target < mid` 中間（左半段正序）  

再試一次，當 `target = 0`  
第一輪搜尋： 4 5 6 **7** 0 1 2，`target` 在右半段，因為左半段是正序，但正序的範圍內不包含 `target`。  

再試一次，當 `target = 3`  
第一輪搜尋： 4 5 6 **7** 0 1 2，`target` 在右半段，因為左半段是正序，但正序的範圍內不包含 `target`。  
第二輪搜尋： 0 **1** 2，`target` 在右半段，因為他介於左半段是正序，但範圍內不包含 `target`。  
第三輪搜尋： 2，最後剩一個數字，`target` 不等於這個數字，則返回 `-1`。  
  
----

感覺可行？再旋轉看看！  
Input: `nums = [6,7,0,1,2,4,5]`  
當 `target = 4`  
第一輪搜尋： 6 7 0 **1** 2 4 5，切一半後來看， `target` 可能在哪裡？在右邊，因為他介於 `mid < target < right` 中間（右半段正序）  

再試一次，當 `target = 0`  
第一輪搜尋： 6 7 0 **1** 2 4 5，`target` 在左半段，因為右半段是正序，但正序的範圍內不包含 `target`。  

再試一次，當 `target = 8`  
第一輪搜尋： 4 5 6 **7** 0 1 2，`target` 在左半段，因為右半段是正序，但正序的範圍內不包含 `target`。  
第二輪搜尋： 4 **5** 6 7  
👉 `target` 在右半段，因為左半段是正序，但正序的範圍內不包含 `target`。  
或  
👉 `target` 在左半段，因為右半段是正序，但正序的範圍內不包含 `target`。  
以上兩者得到的結論會一樣，找不到 `target`。  

----
 
整理一下：  

在判斷第二輪要往往左半邊還是右半邊找的時候，需要多把 `target` 這個因素考量進去：  
```python
if (nums[mid] == target): return mid
elif (左半段是正序 and 右半段是正序): # 沒有旋轉的狀況
    if (target 在左半範圍):
        right = mid - 1
    elif (target 在右半範圍):
        left = mid + 1
elif (左半段是正序 and 右半段是亂序):
    if (target 在左半段正序範圍內):
        right = mid - 1
    else:
        left = mid + 1
elif (右半段是正序 and 左半段是亂序):
    if (target 在右半段正序範圍內):
        left = mid + 1
    else:
        right = mid - 1
```

整理一下，可以得到：  
```python
if nums[mid] == target:
    return mid
elif  (左半段是正序):
    if (target 在左半段正序範圍內):
        right = mid - 1
    else:
        left = mid + 1
else:
    if (target 在右半段正序範圍內):
        left = mid + 1
    else:
        right = mid - 1
```
整理到上面這樣已經可以了，但如果要再整理，會變成下面這樣：  
```python
if nums[mid] == target:
    return mid
elif (target 在左半正序範圍內) or (左半亂序 and ( target 不在右半正序範圍內 )):
    # 上面這段程式碼會變成
    # (target 在左半正序範圍內) -> nums[left] <= target < nums[mid]
    # (左半亂序 and ( target 不在右半正序範圍內 ))
        # 左半亂序 -> nums[left] > nums[mid]
        # target 不在右半正序範圍內 -> target < nums[mid] (比右半最小值還小) or target >= nums[left] (比右半最大值還大)
    # 整理一下： nums[left] <= target < nums[mid] or nums[left] > nums[mid] > target or target >= nums[left] > nums[mid]
    right = mid - 1
else:
    left = mid + 1
```

**方法: Binary Search**

* 步驟
    1. 初始化 `left`, `right`。
    2. 取 `mid = (left + right) // 2`，比較 `nums[left]`、`nums[mid]`、`nums[right]` 之間的關係。
        - 若 `nums[mid] == nums[right]`: 返回 `mid` 位置。
        - 若 `nums[left] < nums[mid]` (表示左半正序)
            - 若 `nums[left] <= target < nums[mid]` (表示在範圍內): 下一輪搜尋左半段
            - 其他狀況: 下一輪搜尋右半段
        - 若 `nums[mid] < nums[right]` (表示右半正序)
            - 若 `nums[mid] < target <= nums[right]` (表示在範圍內): 下一輪搜尋右半段
            - 其他狀況: 下一輪搜尋左半段

* 複雜度
    * 時間複雜度: O(logN)
    * 空間複雜度: O(1)

# 238. Product of Array Except Self
[題目連結](https://leetcode.com/problems/product-of-array-except-self/)

## 題目描述
原文：

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

----

GPT 4 翻譯：

給定一個整數陣列 nums，返回一個陣列 answer，使得 answer[i] 等於 nums 中除了 nums[i] 以外所有元素的乘積。

nums 的任何前綴或後綴的乘積都保證適合在一個32位整數中。

你必須寫一個算法，該算法的執行時間為 O(n)，且不使用除法操作。

----

Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```


Constraints:

* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`
* The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

## 思路

這題一開始在想的時候，會很直覺的想要把所有數字全部乘在一起得到總和，然後在掃過一次數字，把自己的部分除掉，但題目也明確規定了，不能用除法，代表不能這樣做，那要怎麼做呢？

可以回到重新觀察題目，以隨便一個範例來看 `nums = [0,1,2,3,4,5,6,7,8,9]` ，所以：
```
陣列掃到 0 的時候 => [後面 1 乘到 9]
陣列掃到 1 的時候 => [前面 0 乘到 0] * [後面 2 乘到 9]
陣列掃到 2 的時候 => [前面 0 乘到 1] * [後面 3 乘到 9]
陣列掃到 3 的時候 => [前面 0 乘到 2] * [後面 4 乘到 9]
... 以此類推
陣列掃到 9 的時候 => [前面 0 乘到 8]
```

所以我們可以先製作前半段再製作後半段，在把他們乘在一起。注意，勿忽略以上思考的步驟，在遇到沒想法的題目時，一定要先回到演算法的思維去想，再去觀察他的規律。

**方法 1: 左右累積陣列**

* 步驟
    1. 先做到右掃過一次，不斷的累積並將每一次結果存起來
        ```python
        left[0] = 1  // 初始值
        left[1] = 0
        left[2] = 0*1
        left[3] = 0*1*2
        left[4] = 0*1*2*3
        left[5] = 0*1*2*3*4
        left[6] = 0*1*2*3*4*5
        left[7] = 0*1*2*3*4*5*6
        left[8] = 0*1*2*3*4*5*6*7
        left[9] = 0*1*2*3*4*5*6*7*8
        ```
    2. 再從右到左掃一次，不斷的累積並將每一次結果存起來
        ```python
        right[9] = 1   // 初始值
        right[8] = 9
        right[7] = 9*8
        right[6] = 9*8*7
        right[5] = 9*8*7*6
        right[4] = 9*8*7*6*5
        right[3] = 9*8*7*6*5*4
        right[2] = 9*8*7*6*5*4*3
        right[1] = 9*8*7*6*5*4*3*2
        right[0] = 9*8*7*6*5*4*3*2*1
        ```
    3. 組裝，當 i = x 時，其解為 left[x] * right[x]，注意位置不得超過陣列範圍。

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(N)


**方法 2: 再更優化**

能不能不要有 right ，保留 left 就好呢？觀察一下剛剛的 left 陣列結果：

```python
left[0] = 1  // 初始值
left[1] = 0
left[2] = 0*1
left[3] = 0*1*2
left[4] = 0*1*2*3
left[5] = 0*1*2*3*4
left[6] = 0*1*2*3*4*5
left[7] = 0*1*2*3*4*5*6
left[8] = 0*1*2*3*4*5*6*7
left[9] = 0*1*2*3*4*5*6*7*8
```

right 如果這時候從尾巴往前掃的時候，順序會是數字是 9, 8, 7....，如下：
```
right = 9, ans = left[9] 
right = 8, ans = left[8] * 9
right = 7, ans = left[7] * 9 * 8
right = 6, ans = left[6] * 9 * 8 * 7
...
```

發現了什麼呢？是不是如果第二圈在跑的時候，有一個延遲的累乘 right，不斷的和 left 相乘，就可以得到答案。程式碼如下：

```python
right = 1
for i in range(len(nums) - 1, -1, -1):
    left[i] *= right   // 先乘
    right *= nums[i]   // 再算出累乘的值
```

* 步驟
    1. 先做到右掃過一次，不斷的累積並將每一次結果存起來
        ```python
        ans[0] = 1  // 初始值
        ans[1] = 0
        ans[2] = 0*1
        ans[3] = 0*1*2
        ans[4] = 0*1*2*3
        ans[5] = 0*1*2*3*4
        ans[6] = 0*1*2*3*4*5
        ans[7] = 0*1*2*3*4*5*6
        ans[8] = 0*1*2*3*4*5*6*7
        ans[9] = 0*1*2*3*4*5*6*7*8
        ```
    2. 再從右到左掃一次，將結果直接對 ans 處理，如下：
        ```python
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right    // 先乘
            right *= nums[i]   // 再算出累乘的值
        ```

* 複雜度
    * 時間複雜度: O(N)
    * 空間複雜度: O(1)   // 不計入 ans 所使用的陣列


## 本題學習
1. 在遇到題目沒想法時，可以回到演算法的思維，隨便列一個長一點的 input ，然後讓自己像一個 for loop 一樣，從左掃到右試試看，觀察一下是否有規律存在。
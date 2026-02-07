# 代码随想录算法训练营第 43 天 | 第九章 动态规划 part10

## 子序列系列（入门）

今天正式进入子序列系列，先做两道相对简单的题，感受一下子序列题目的思路。建议先做 674 再做 300，体会「连续」与「不连续」的区别。

## Leetcode 300. 最长递增子序列

#### 题目链接：[题目](https://leetcode.cn/problems/longest-increasing-subsequence/)

#### 思路：
- **dp 数组在 track 什么**：`dp[i]` 表示 **以 `nums[i] 结尾`** 的、最长递增子序列的长度（LIS 必须包含当前这个数）。
- 用两个 loop：外层枚举结尾位置 `i`，内层枚举「前面的位置 `j`」（j < i）。若 `nums[j] < nums[i]`，说明可以把 `nums[i]` 接在以 `nums[j]` 结尾的递增子序列后面，则 `dp[i] = max(dp[i], dp[j] + 1)`。
- 初始化：每个位置单独成一段长度为 1，即 `dp[i] = 1`。最后答案是 `max(dp)`，因为最长 LIS 可能以任意位置结尾。


```Python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1ng411J7xP)
- [文章讲解](https://programmercarl.com/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.html)

---

## Leetcode 674. 最长连续递增序列

#### 题目链接：[题目](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/)

#### 思路：
和 300 的最大区别在于「连续」。先自己写一写，体会和 300 的差异。

这道题是连续的，所以直接和之前比较就行了


```Python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        current_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_len += 1
                max_len = max(current_len, max_len)
            else:
                current_len = 1

        return max_len
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1bD4y1778v)
- [文章讲解](https://programmercarl.com/0674.%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD%E9%80%92%E5%A2%9E%E5%BA%8F%E5%88%97.html)

---

## Leetcode 718. 最长重复子数组

#### 题目链接：[题目](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/)

#### 思路：
稍难一些，需要用到二维 dp 数组。因为要更新两个 Array


```Python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])


        return max_len
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV178411H7hV)
- [文章讲解](https://programmercarl.com/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.html)

## 总结


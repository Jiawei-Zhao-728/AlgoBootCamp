# 代码随想录算法训练营第 43 天 | 第九章 动态规划 part11

## 子序列与子数组

体会 1143 和 718 的区别（子序列 vs 连续子数组）；1035 和 1143 本质相同；53 用 dp 再做一遍最大子序和；392 是编辑距离的入门（只涉及“删除”）。

## Leetcode 1143. 最长公共子序列

#### 题目链接：[题目](https://leetcode.cn/problems/longest-common-subsequence/)

#### 思路：
体会本题和 718. 最长重复子数组 的区别（子序列可以不连续）。

还是差不多的意思，就是我们要选择，如果选择，那么我们就 dp【-1】 + 1 如果不是，就选择之前的最好 option。

```Python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1ye4y1L7CQ)
- [文章讲解](https://programmercarl.com/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.html)

---

## Leetcode 1035. 不相交的线

#### 题目链接：[题目](https://leetcode.cn/problems/uncrossed-lines/)

#### 思路：
和 1143. 最长公共子序列 一模一样，可以自己先做一遍。

一模一样代码 

```Python
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1h84y1x7MP)
- [文章讲解](https://programmercarl.com/1035.%E4%B8%8D%E7%9B%B8%E4%BA%A4%E7%9A%84%E7%BA%BF.html)

---

## Leetcode 53. 最大子序和

#### 题目链接：[题目](https://leetcode.cn/problems/maximum-subarray/)

#### 思路：
贪心做过一次，这次用 dp 再做一遍。
思路就是，更新


```Python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sub = nums[0]

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)

        return max_sub
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV19V4y1F7b5)
- [文章讲解](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)

---

## Leetcode 392. 判断子序列

#### 题目链接：[题目](https://leetcode.cn/problems/is-subsequence/)

#### 思路：
编辑距离的入门题（这里只涉及“删除”），为后面的编辑距离打基础。



```Python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0 , 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
```

#### 参考
- [文章讲解](https://programmercarl.com/0392.%E5%88%A4%E6%96%AD%E5%AD%90%E5%BA%8F%E5%88%97.html)

## 总结


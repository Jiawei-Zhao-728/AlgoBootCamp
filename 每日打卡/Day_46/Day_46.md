# 代码随想录算法训练营第 46 天 | 第九章 动态规划 part13

## 回文与动态规划收尾

今天我们就要结束动态规划章节了，大家激不激动！！！

## Leetcode 647. 回文子串

#### 题目链接：[题目](https://leetcode.cn/problems/palindromic-substrings/)

#### 思路：
动态规划解决的经典题目。如果没接触过的话，别硬想，直接看题解。


```Python
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 中心扩展法：

        n = len(s)
        count = 0

        def center (l, r):
            cnt = 0

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1

            return cnt

        for i in range(n):
            count += center(i, i)
            count += center(i, i + 1)

        return count
```

#### 参考
- [文章讲解](https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html)

---

## Leetcode 516. 最长回文子序列

#### 题目链接：[题目](https://leetcode.cn/problems/longest-palindromic-subsequence/)

#### 思路：
647 求的是**回文子串**，本题要求的是**回文子序列**，要搞清楚两者之间的区别（子串连续、子序列可不连续）。

这道题其实蛮难的，这个 dp Array 的概念蛮神奇

```Python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
```

#### 参考
- [文章讲解](https://programmercarl.com/0516.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E5%BA%8F%E5%88%97.html)

---

## 动态规划总结篇

做一个总结吧。

#### 参考
- [动态规划总结篇](https://programmercarl.com/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E6%80%BB%E7%BB%93%E7%AF%87.html)

## 总结


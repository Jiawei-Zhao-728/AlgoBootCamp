# 代码随想录算法训练营第 41 天 | 第九章 动态规划 part08

## 买卖股票系列（入门）

股票问题是一个动态规划的系列问题，前两题并不难，第三题有难度。

## Leetcode 121. 买卖股票的最佳时机

#### 题目链接：[题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

#### 思路：

比较 basic 的一个 dp


```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = 0

        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)

        return max_price
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1Xe4y1u77q)
- [文章讲解](https://programmercarl.com/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.html)

---

## Leetcode 122. 买卖股票的最佳时机 II

#### 题目链接：[题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

#### 思路：

这里会用到 2d dp，因为每次我们有两个选择


```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # not hold
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # hold
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1D24y1Q7Ls)
- [文章讲解](https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html)

---

## Leetcode 123. 买卖股票的最佳时机 III

#### 题目链接：[题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/)

#### 思路：
这道题一下子就难度上来了，关键在于**至多买卖两次**：可以买卖一次、可以买卖两次、也可以不买卖。状态和转移要按「最多完成几笔」来设计，为后面 188（k 笔）打基础。

认识到有五个 state


```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1 :
            return 0
        dp = [[0] * 5 for _ in range(n)]

        # don't buy any
        dp[0][0] = 0
        # buy one:
        dp[0][1] = -prices[0]
        # sell one:
        dp[0][2] = 0
        # buy two:
        dp[0][3] = -prices[0]
        # sell two:
        dp[0][4] = 0

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            # buy 1
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # sell 1
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            # buy 2
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            # sell 2:
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return dp[n - 1][4]
            



```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1WG411K7AR)
- [文章讲解](https://programmercarl.com/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.html)

## 总结


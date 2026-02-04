# 代码随想录算法训练营第 41 天 | 第九章 动态规划 part09

## 买卖股票系列（进阶）

188 是 123 的进阶版；309 含冷冻期，状态更多要区分清楚；714 在 122 基础上只需在卖出时减去手续费，代码几乎一样，可以独立尝试。

## Leetcode 188. 买卖股票的最佳时机 IV

#### 题目链接：[题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/)

#### 思路：

- **题意**：最多完成 **k 笔**交易（一笔 = 一次买 + 一次卖），求最大利润。是 123 题「最多 2 笔」的推广。
- **状态**：
  - `buy[j]`：到当前天为止，**最多完成 j 笔交易**且**当前持有股票**时的最大利润（这里「持有」表示第 j 笔的买已发生，卖还未发生）。
  - `sell[j]`：到当前天为止，**最多完成 j 笔交易**且**当前不持有股票**时的最大利润。
- **转移**（从左到右扫每一天，对 j 从 k 到 1 逆序更新，避免同一轮内 j 用到已更新的 j-1）：
  - 今天**不持有**：要么昨天就不持有 `sell[j]`，要么今天卖出 `buy[j] + prices[i]` → `sell[j] = max(sell[j], buy[j] + prices[i])`。
  - 今天**持有**：要么昨天就持有 `buy[j]`，要么今天买入（新开第 j 笔，从「最多 j-1 笔且不持有」转移）→ `buy[j] = max(buy[j], sell[j-1] - prices[i])`。
- **初始化**：`buy[j] = -prices[0]`（第 0 天买入），`sell[j] = 0`。
- **特判**：若 `k >= n/2`，相当于不限制次数，等价于 122 题，直接累加所有正差价即可。

```Python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)

        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        
        buy = [-prices[0]] * (k + 1)
        sell = [0] * (k + 1)

        for i in range(1, n):
            for j in range(k, 0, -1):
                sell[j] = max(sell[j], buy[j] + prices[i])
                buy[j] = max(buy[j], sell[j - 1] - prices[i])
        

        return sell[k]
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV16M411U7XJ)
- [文章讲解](https://programmercarl.com/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.html)

---

## Leetcode 309. 最佳买卖股票时机含冷冻期

#### 题目链接：[题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

#### 思路：
含冷冻期，状态会变多，要把状态区分清楚，思路才清晰。把 sell 和 buy 分清楚。 


```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        n = len(prices)

        # init:
        buy = [0] * n
        sell = [0] * n 

        # buy in at 0 day
        buy[0] = -prices[0]
        # nothing to sell
        sell[0] = 0
        
        # buy in at day 1 or day 0
        buy[1] = max(-prices[0], -prices[1])
        # sell has two option, don't sell or sell the one bought at day 0
        sell[1] = max(0, prices[1] - prices[0])

        for i in range(2, n):
            buy[i] = max(buy[i - 1], sell[i - 2 ] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return sell[n - 1]

```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1rP4y1D7ku)
- [文章讲解](https://programmercarl.com/0309.%E6%9C%80%E4%BD%B3%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E6%97%B6%E6%9C%BA%E5%90%AB%E5%86%B7%E5%86%BB%E6%9C%9F.html)

---

## Leetcode 714. 买卖股票的最佳时机含手续费

#### 题目链接：[题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

#### 思路：
和 122 类似，只需在计算「卖出」时减去手续费即可，代码几乎一样，建议先独立做一遍。


```Python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        if n == 0:
            return 0

        hold = [0] * n
        sell = [0] * n

        hold[0] = -prices[0]
        sell[0] = 0


        for i in range(1, n):
            # we choose not doing anying, keep holding, or sell the before and buy
            hold[i] = max(hold[i - 1], sell[i -1] - prices[i])
            sell[i] = max(sell[i -1], hold[i - 1] + prices[i] - fee)

        return sell[n - 1]
```

#### 参考
- [视频讲解](https://www.bilibili.com/video/BV1z44y1Z7UR)
- [文章讲解](https://programmercarl.com/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9.html)

---

## 股票总结

#### 参考
- [动态规划-股票问题总结篇](https://programmercarl.com/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92-%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93%E7%AF%87.html)

## 总结
股票，更好理解了

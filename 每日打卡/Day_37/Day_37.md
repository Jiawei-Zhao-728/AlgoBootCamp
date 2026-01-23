# 代码随想录算法训练营第 37 天| 动态规划 part05 - 完全背包问题

## 完全背包理论基础

力扣上没有纯粹的完全背包的题目，我在卡码网上制作了题目，大家可以去做一做，题目链接在下面的文章链接里。

后面的两道题目，都是完全背包的应用，做做感受一下。

#### 文章讲解: [完全背包理论基础](https://programmercarl.com/背包理论基础/背包理论基础完全背包.html)

#### 思路：
完全背包


```Python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =  [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] +=dp[x - coin]

        
        return dp[amount]

```

## Leetcode 518. 零钱兑换 II

#### 题目链接: [题目](https://leetcode.cn/problems/coin-change-ii/)

#### 思路:
完全背包


```Python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =  [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] +=dp[x - coin]

        
        return dp[amount]

```

## Leetcode 377. 组合总和 IV

#### 题目链接: [题目](https://leetcode.cn/problems/combination-sum-iv/)

#### 思路：
无线背包，但是线 interate 这个金额


```Python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1): 
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[target]
```

## 70. 爬楼梯(进阶)

这道题目爬楼梯之前我们做过，这次再用完全背包的思路来分析一遍

#### 文章讲解: [爬楼梯完全背包版本](https://programmercarl.com/0070.爬楼梯完全背包版本.html)

#### 思路:

巧妙呢


```Python
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]

        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            for step in steps:
                if i >= step:
                    dp[i] += dp[i - step]


        return dp[n]
```

## 总结



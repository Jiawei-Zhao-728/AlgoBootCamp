# 代码随想录算法训练营第 38 天| Leetcode 322. 零钱兑换, Leetcode 279. 完全平方数, Leetcode 139. 单词拆分

## Leetcode 322. 零钱兑换

#### 题目链接： [题目](https://leetcode.cn/problems/coin-change/)

#### 思路：

这要是一个找 prior best solution，然后通过coin 的面值来判断。


```Python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:

                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        
        return dp[amount] if dp[amount] != float('inf') else -1




```

## Leetcode 279. 完全平方数

#### 题目链接: [题目](https://leetcode.cn/problems/perfect-squares/)

#### 思路:

思路其实和 coin 一样，我们其实就是做一个完全背包。


```python
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in squares:
                if j <= i:
                    dp[i] = min(dp[i - j] + 1, dp[i])


        return dp[n]


```

## Leetcode 139. 单词拆分

#### 题目链接: [题目](https://leetcode.cn/problems/word-break/)

#### 思路：


```Python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1): 
            for word in wordDict:
                word_len = len(word)

                if i >= word_len and dp[i - word_len]:
                    if s[i - word_len : i ] == word:
                        dp[i] = True

                        break
        
        return dp[n]
```

## 关于多重背包

你该了解这些！

#### 文章讲解: [背包问题集合](https://programmercarl.com/背包问题集合.html)

## 背包问题总结篇

#### 文章讲解: [背包总结篇](https://programmercarl.com/背包总结篇.html)

## 总结



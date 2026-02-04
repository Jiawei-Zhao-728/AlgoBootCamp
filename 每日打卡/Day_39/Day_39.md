# 代码随想录算法训练营第 39 天| Leetcode 198. 打家劫舍, Leetcode 213. 打家劫舍 II, Leetcode 337. 打家劫舍 III

## 打家劫舍系列

今天就是打家劫舍的一天，这个系列不算难，大家可以一口气拿下。

## Leetcode 198. 打家劫舍

#### 题目链接： [题目](https://leetcode.cn/problems/house-robber/)

#### 思路：


```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
```

## Leetcode 213. 打家劫舍 II

#### 题目链接: [题目](https://leetcode.cn/problems/house-robber-ii/)

#### 思路:


```Python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr:List[int]) -> int:
            prev2, prev1 = 0, 0
            for x in arr:
                cur = max(prev1, prev2 + x) 
                prev2, prev1 = prev1, cur 
            return prev1

        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

## Leetcode 337. 打家劫舍 III

#### 题目链接: [题目](https://leetcode.cn/problems/house-robber-iii/)

#### 思路：
核心递归逻辑

对于每个节点，我们要计算"从这个节点开始往下能抢到的最大金额"。有两个互斥的选择：

选择1：抢劫当前节点

rob_current = 当前节点的值 + 四个孙子节点能抢到的最大值

为什么是孙子节点？因为抢了当前节点，就不能抢左右子节点，但可以抢孙子节点。

选择2：不抢劫当前节点

not_rob = 左子节点能抢到的最大值 + 右子节点能抢到的最大值
不抢当前节点，那么左右子节点可以自由选择抢或不抢。


```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs (node):
            if not node:
                return 0
            if node in memo:
                return memo[node]

            # stra 1: rub
            rob_current = node.val
            if node.left:
                rob_current += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_current += dfs(node.right.left) + dfs(node.right.right)

            # stra 2: do not rub
            not_rub = dfs(node.left) + dfs(node.right)

            memo[node] = max(not_rub, rob_current)

            return memo[node]

        return dfs(root)
        
```

## 总结



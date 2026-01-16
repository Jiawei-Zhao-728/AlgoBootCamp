# 代码随想录算法训练营第 33 天| 动态规划 part01

## 理论基础

无论大家之前对动态规划学到什么程度，**一定要先看我讲的动态规划理论基础**。

如果没做过动态规划的题目，看我讲的理论基础，会有感觉是不是简单题想复杂了？其实并没有，我讲的理论基础内容，在动规章节所有题目都有运用，所以很重要！

如果做过动态规划题目的录友，看我的理论基础就会感同身受了。

## Leetcode 509. 斐波那契数

#### 题目链接： [题目](https://leetcode.cn/problems/fibonacci-number/)

#### 思路：
基础 fib


```Java
class Solution {
    public int fib(int n) {
        if (n <= 1) return n; 

        int prev1 = 0; 
        int prev2 = 1;

        for (int i = 2; i <= n; i++){
            int cur = prev1 + prev2; 

            prev1 = prev2; 
            prev2 = cur;

        }

        return prev2; 
    }
}
```

## Leetcode 70. 爬楼梯

#### 题目链接: [题目](https://leetcode.cn/problems/climbing-stairs/)

#### 思路:
这道题其实和 fib 一样，一样的道理


```Java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n; 
        int [] dp_arr = new int[n + 1]; 
        dp_arr[1] = 1; 
        dp_arr[2] = 2; 

        for (int i = 3; i <= n; i ++){
            dp_arr[i] = dp_arr[i - 1] + dp_arr[i - 2]; 
        }

        return dp_arr[n]; 
    }
}
```

## Leetcode 746. 使用最小花费爬楼梯

#### 题目链接: [题目](https://leetcode.cn/problems/min-cost-climbing-stairs/)

#### 思路：
这道题就是一个 min 之前的两个 step，然后加上现在的 cost。 

```Java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length; 
        if (n <= 2) return Math.min(cost[0], cost[1]); 

        int [] dp = new int[n]; 
        dp[0] = cost[0]; 
        dp[1] = cost[1]; 

        for (int i = 2; i < n; i ++){
            dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
        }

        return Math.min(dp[n - 1], dp[n - 2]); 
    }
}
```

## 总结



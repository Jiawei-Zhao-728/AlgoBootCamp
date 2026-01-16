# 代码随想录算法训练营第 34 天| Leetcode 62. 不同路径, Leetcode 63. 不同路径 II, Leetcode 343. 整数拆分, Leetcode 96. 不同的二叉搜索树

## Leetcode 62. 不同路径

#### 题目链接： [题目](https://leetcode.cn/problems/unique-paths/)

#### 思路：


```Java
class Solution {
    public int uniquePaths(int m, int n) {
        // 2d dp: 
        int [] [] dp = new int [m][n]; 

        // init
        for ( int i = 0; i < m; i ++){
            dp[i][0] = 1; 
        }

        for (int i = 0; i < n; i ++){
            dp[0][i] = 1; 
        }

        for(int i = 1; i < m; i ++){
            for (int j = 1; j < n; j ++){
                dp[i][j] = dp[i -1][j] + dp[i][j - 1]; 
            }
        }

        return dp[m - 1][n - 1];


    }
}
```

## Leetcode 63. 不同路径 II

#### 题目链接: [题目](https://leetcode.cn/problems/unique-paths-ii/)

#### 思路:

这道题要考虑到obstical，所以有 opstical 的地方是 0，就好了。


```Java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length; 

        // 如果起点或终点是障碍物，直接返回 0
        if (obstacleGrid[0][0] == 1 || obstacleGrid[m-1][n-1] == 1) {
            return 0;
        }

        int [][] dp = new int[m][n];
        dp[0][0] = 1; 

        // 初始化第一行

        for (int i = 1; i < n; i ++){
            if (obstacleGrid[0][i] ==1){
                dp[0][i] = 0; 
            }else{
                dp[0][i] = dp[0][i - 1];
            }

        }
        // 初始化第一列

        for (int i = 1; i < m; i ++){
            if (obstacleGrid[i][0] == 1){
                dp[i][0] = 0;
            }else{
                dp[i][0] = dp[i - 1][0]; 
            }
        }

        for (int i = 1; i < m; i ++){
            for (int j = 1; j < n; j ++){
                if (obstacleGrid[i][j] == 1 ){
                    dp[i][j] = 0;
                }else{
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }

        return dp[m - 1][n - 1]; 
        
    }
}
```

## Leetcode 343. 整数拆分（可跳过）

#### 题目链接: [题目](https://leetcode.cn/problems/integer-break/)

#### 思路：


```Java

```

## Leetcode 96. 不同的二叉搜索树（可跳过）

#### 题目链接: [题目](https://leetcode.cn/problems/unique-binary-search-trees/)

#### 思路:


```Java

```

## 总结



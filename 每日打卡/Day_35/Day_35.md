# 代码随想录算法训练营第 35 天| 动态规划 part03 - 01 背包问题

## 背包问题理论

背包问题其实挺难的，虽然大家看到模板代码会感觉很清晰，但如果没有亲身去思考的话，理解还是会有问题的。

如果没做过背包问题，建议大家先看文字讲解，把背包问题理论基础理解透彻了。如果做过背包类题目，也可以看一下视频，视频里讲了很多细节，是文字详解涉及不到的。

力扣上没有纯 01 背包的问题，所以大家看背包理论基础的时候，先了解一下 01 背包，理解透彻，然后再做具体题目。

## 01 背包问题 二维

#### 文章讲解: [背包问题理论基础](https://programmercarl.com/背包理论基础/背包理论基础.html)

#### 思路：

这道题真的蛮难的，理解一下这个 inner loop 的逻辑就要了蛮久的时间

```Java
import java.util.Scanner; 

public class Main{
    public static void main (String [] args){ 
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt(); 
        
        int[] space = new int[M]; 
        int[] value = new int[M];

        for (int i = 0; i < M; i ++ ) {
            space[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
            value[i] = sc.nextInt(); 
        }

        int [] dp = new int [N + 1];

        for (int i = 0; i < M; i ++) {
            for (int j = N; j >= space[i]; j -- ){
                dp[j] = Math.max(dp[j], dp[j - space[i]] + value[i]);
            }
        }

        System.out.println(dp[N]);
        sc.close();
    }
}
```

## 01 背包问题 一维（滚动数组）

#### 文章讲解: [背包问题理论基础](https://programmercarl.com/背包理论基础/背包理论基础.html)

#### 思路:

这种 dp 真的蛮巧妙，就是需要 小 loop 去凑，真的很巧妙

```Java
import java.util.Scanner; 

public class Main{
    public static void main (String [] args){ 
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt(); 
        
        int[] space = new int[M]; 
        int[] value = new int[M];

        for (int i = 0; i < M; i ++ ) {
            space[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
            value[i] = sc.nextInt(); 
        }

        int [] dp = new int [N + 1];

        for (int i = 0; i < M; i ++) {
            for (int j = N; j >= space[i]; j -- ){
                dp[j] = Math.max(dp[j], dp[j - space[i]] + value[i]);
            }
        }

        System.out.println(dp[N]);
        sc.close();
    }
}
```

## Leetcode 416. 分割等和子集

#### 题目链接: [题目](https://leetcode.cn/problems/partition-equal-subset-sum/)

#### 思路：

```Java
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0; 
        for (int num: nums){
            sum += num; 
        }

        // if odd, then cant be split
        if ( sum % 2 != 0){
            return false; 
        }

        int target = sum / 2; 

        boolean [] dp = new boolean[target + 1 ];

        dp[0] = true; 
        for (int numb: nums){
            for ( int j = target; j >=  numb; j --){
                dp[j] = dp[j] || dp[j - numb];
            }
        }

        return dp[target];
    }
}
```

## 总结

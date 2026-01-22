# 代码随想录算法训练营第 36 天| Leetcode 1049. 最后一块石头的重量 II, Leetcode 494. 目标和, Leetcode 474. 一和零

## Leetcode 1049. 最后一块石头的重量 II

#### 题目链接： [题目](https://leetcode.cn/problems/last-stone-weight-ii/)

#### 思路：

同样的 0-1 背包， 真的蛮难的。 

```Java
class Solution {
    public int lastStoneWeightII(int[] stones) {
        int sum = 0; 
        for (int stone : stones){
            sum += stone; 
        }

        int target = sum / 2;
        int [] dp = new int[target + 1]; 
        
        for (int stone : stones){
            for (int j = target; j >= stone; j --){
                dp[j] = Math.max(dp[j], dp[j- stone] + stone); 
            }
        }

        return sum - 2  * dp[target]; 


    }
}
```

## Leetcode 494. 目标和

#### 题目链接: [题目](https://leetcode.cn/problems/target-sum/)

#### 思路:

```Java
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0; 
        for (int i : nums){
            sum += i; 
        }

        if (sum < Math.abs(target)) return 0; 
        if ((sum + target) % 2 != 0) return 0;

        int bagSize = (sum + target) / 2;

        int [] dp = new int[bagSize + 1];
        dp[0] = 1 ;

        for (int n : nums){
            for (int j = bagSize; j >= n; j --){
                dp[j] += dp[j - n]; 
            }
        }

        return dp[bagSize];



    }
}
```

## Leetcode 474. 一和零

#### 题目链接: [题目](https://leetcode.cn/problems/ones-and-zeroes/)

#### 思路：

这是 二维费用的 0-1 背包 问题，比一维背包多一层循环。

必须从后向前更新，保证每个字符串只被选择一次。

状态定义：dp[i][j] 表示最多用 i 个 0 和 j 个 1 时的最大子集长度。

```Java
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs: 
            zeros =  s.count('0')
            ones = len(s) - zeros

            # 01 背包：
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        
        return dp[m][n]


```

## 总结

# 代码随想录算法训练营第 28 天| Leetcode 122. 买卖股票的最佳时机 II, Leetcode 55. 跳跃游戏, Leetcode 45. 跳跃游戏 II, Leetcode 1005. K 次取反后最大化的数组和

## Leetcode 122. 买卖股票的最佳时机 II

#### 题目链接： [题目](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

#### 思路：

这道题就是把所有的上升期算起来

```Java
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0; 
        for ( int i = 1; i < prices.length; i ++){
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) profit += diff;
        }

        return profit; 
    }
}
```

## Leetcode 55. 跳跃游戏

#### 题目链接: [题目](https://leetcode.cn/problems/jump-game/)

#### 思路:

这道题其实只是需要一直跳 max。

```Java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        int n = nums.length; 

        for (int i = 0; i < n; i ++){
            // cant reach current place
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]); 
            if (maxReach >= n - 1) return true;

        }

        return false;
    }
}
```

## Leetcode 45. 跳跃游戏 II

#### 题目链接: [题目](https://leetcode.cn/problems/jump-game-ii/)

#### 思路：

这道题感觉蛮难的，要理解怎么每个 step cover 哪几段，画图好理解一点。

```Java
class Solution {
    public int jump(int[] nums) {
        int step = 0; 
        int curEnd = 0;
        int farthrest = 0;

        for (int i = 0; i < nums.length - 1; i ++){
            // how far can we jump from current place: 
            farthrest = Math.max(farthrest, i + nums[i]);

            if (i == curEnd) {
                step ++; 
                curEnd = farthrest; 
            }

        }

        return step; 
    }
}
```

## Leetcode 1005. K 次取反后最大化的数组和

#### 题目链接: [题目](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/)

#### 思路:

这个其实就是把负数 flip，然后如果还有 k，就把最小的正数 flip。然后求和。

```Java
class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);

        for (int i = 0; i < nums.length && k > 0 && nums[i] < 0; i ++){
            nums[i] = -nums[i];
            k --;
        }

        if (k > 0){
            Arrays.sort(nums);
            if (k % 2 == 1){
                nums[0] = -nums[0];
            }
        }

        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;

    }
}
```

## 总结

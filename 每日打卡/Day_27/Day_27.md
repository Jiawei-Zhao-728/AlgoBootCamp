# 代码随想录算法训练营第 27 天| 贪心算法 part01

## 理论基础

贪心算法其实没有什么规律可言，了解它没有规律的本质就够了。不用花心思去研究其规律，**没有思路就立刻看题解**。

基本贪心的题目有两个极端，要不就是特简单，要不就是死活想不出来。学完贪心之后再去看动态规划，就会了解贪心和动规的区别。

## Leetcode 455. 分发饼干

#### 题目链接： [题目](https://leetcode.cn/problems/assign-cookies/)

#### 思路：

排序后，如果当前最小的饼干不能满足当前最小的孩子，那么它肯定不能满足后面胃口更大的孩子，所以直接跳过这块饼干是安全的。

如果能满足，则用这块饼干满足当前孩子，因为如果不用它，后面可能没有更小的饼干去满足这个孩子，而这块饼干如果留给后面的孩子，可能造成浪费（后面的孩子胃口更大，可能不需要这块小的）。

```Java
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);


        int i = 0;
        int j = 0;
        int count = 0;

        while (i < g.length && j < s.length){
            if (s[j] >= g[i]){
                count ++;
                i ++;
                j ++;
            } else {
                j ++;
            }
        }

        return count;
    }

}
```

## Leetcode 376. 摆动序列

#### 题目链接: [题目](https://leetcode.cn/problems/wiggle-subsequence/)

#### 思路:

只要当前数字与前一个数字的差（diff = nums[i] - nums[i-1]）与前一个有效差的方向相反，就说明出现了摆动

```Java
 class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2){
            return nums.length;
        }

        int prev_diff = 0;
        int count = 1;

        for (int i = 1; i < nums.length; i ++){
            int cur_diff = nums[i] - nums[i - 1];

            // when the sign changes, increment count:
            if ((prev_diff <= 0 && cur_diff > 0) || (prev_diff >= 0 && cur_diff < 0) ){
                count ++;
                prev_diff = cur_diff;
            }
        }

        return count;
    }
}
```

## Leetcode 53. 最大子序和

#### 题目链接: [题目](https://leetcode.cn/problems/maximum-subarray/)

#### 思路：
如果当前子数组的和变为负数，它只会拖累后面的元素，所以应该丢弃，从当前元素重新开始计算

```Java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = 0; 

        for (int i : nums){
            currentSum = Math.max(i, currentSum + i);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
```


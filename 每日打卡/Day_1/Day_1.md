# 代码随想录算法训练营第一天| 704. 二分查找、27. 移除元素, Leetcode 977 有序数组的平方

## Leetcode 704 二分查找

#### 题目链接： [题目](https://leetcode.cn/problems/binary-search/)

#### 思路

这道题算是比较核心而且基础的二分查找算法。我觉得直觉就是当看到一个数组是 sorted，那么就要有想到二分查找的想法，因为二分查找的核心的就是一个 sorted Array。
技术上的难点来说， 我觉得就是两点， 第一是计算 mid 的公式， 第二就是判断大小。除此之外应该都还好。

```Java
class Solution {
    public int search(int[] nums, int target) {

        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target){
                return m;
            }else if (nums[m] > target){
                r = m - 1;
            }else{
                l = m + 1;
            }
        }

        return -1;
    }
}
```

## Leetcode 27 移除元素

#### 题目链接: [题目](https://leetcode.cn/problems/remove-element/description/)

#### 思路:

这道题的思路一开始是两个 pointer，那么两个 pointer 应该怎么去处理呢？更多是一个快慢 pointer 的概念，有一个快在前面去找不一样的，一个慢的 pointer 在后面 track 所有 target。然后如果需要 swap，我们就快慢去做 swap。
快慢 pointer 也可以作为找一条链表中点的方法。

```Java
class Solution {
    public int removeElement(int[] nums, int val) {
        int j = 0;

        for (int i = 0; i < nums.length; i++){
            if (nums[i] != val){
                nums[j] = nums[i];
                j ++;

            }
        }

        return j;
    }
}
```

## Leetcode 977 有序数组的平方

#### 题目链接: [题目](https://leetcode.cn/problems/squares-of-a-sorted-array/description/)

#### 思路：

这道题最主要就是要意识到一开始的 Array 也是 sorted，那么有一个很重要的关系就是，如果如果这个 Array 拥有负数，那么两边的平方都可能是最大的，然后中间的一定是最小的，所以我们中两边往中间 populate，而且是从大到小去 populate，这样子就不会有错。

```Java
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int l = 0, r = n -1;
        int index = n -1;


        while (l <= r){
            int l_numb = nums[l] * nums[l];
            int r_numb = nums[r] * nums[r];

            if (l_numb > r_numb){
                res[index] = l_numb;
                l ++;

            }else{
                res[index] = r_numb;
                r --;
            }
            index --;
        }

        return res;
    }
}
```

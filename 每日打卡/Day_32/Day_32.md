# 代码随想录算法训练营第 32 天| Leetcode 56. 合并区间, Leetcode 738. 单调递增的数字, Leetcode 968. 监控二叉树

## Leetcode 56. 合并区间

#### 题目链接： [题目](https://leetcode.cn/problems/merge-intervals/)

#### 思路：

思路和志气啊你的差不多，其实就是一个 sort 然后 iterate

```Java
class Solution {
    public int[][] merge(int[][] intervals) {
        // corner case
        if (intervals == null || intervals.length == 0){
            return new int[0][]; 
        }

        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

        List<int[]> merged = new ArrayList<>(); 
        for (int[] interval : intervals){
            int start = interval[0]; 
            int end = interval[1]; 

            // when adding new merge: 
            if (merged.isEmpty() || start > merged.get(merged.size() - 1)[1]){
                merged.add(new int[]{start, end});
            }else{
                int [] lastInterval = merged.get(merged.size() - 1);
                lastInterval[1] = Math.max(lastInterval[1], end); 
            } 
        }

        return merged.toArray(new int[merged.size()][]); 
    }
}
```

## Leetcode 738. 单调递增的数字

#### 题目链接: [题目](https://leetcode.cn/problems/monotone-increasing-digits/)

#### 思路:

这道题，就是 loop， 找到最小那个违反的那个 digit，然后把它 decrement 一次，然后后面的全部改成 99

```Java
class Solution {
    public int monotoneIncreasingDigits(int n) {
        char [] intArr = Integer.toString(n).toCharArray(); 
        int mark = intArr.length; 

        for (int i = intArr.length - 1; i > 0; i --){
            if (intArr[i] < intArr[i -1]){
                intArr[i - 1] --;
                mark = i;
            }
        }

        for (int i = mark; i < intArr.length; i ++){
            intArr [i] = '9';
        }

        return Integer.parseInt(new String(intArr)); 
    }
}
```

## Leetcode 968. 监控二叉树（可跳过）

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-cameras/)

#### 思路：

```Java

```

## 贪心算法总结

可以看看贪心算法的总结，贪心本来就没啥规律，能写出个总结篇真的不容易了。

## 总结

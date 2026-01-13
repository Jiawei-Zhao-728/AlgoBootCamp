# 代码随想录算法训练营第 31 天| Leetcode 452. 用最少数量的箭引爆气球, Leetcode 435. 无重叠区间, Leetcode 763. 划分字母区间

## 重叠区间问题

今天的三道题目，都算是重叠区间问题，大家可以好好感受一下。都属于那种看起来好复杂，但一看贪心解法，惊呼：这么巧妙！

这种题还是属于那种，做过了也就会了，没做过就很难想出来。不过大家把如下三题做了之后，重叠区间基本上差不多了。

## Leetcode 452. 用最少数量的箭引爆气球

#### 题目链接： [题目](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

#### 思路：
这道题其实很巧妙，其实就是看后面的 start 在不在前的 end 里面。

```Java
class Solution {
    public int findMinArrowShots(int[][] points) {
        
        if (points == null || points.length == 0){
            return 0; 
        }
        // sorting using end: 
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

        // init:
        int arrows = 1; 
        int end = points[0][1]; 

        // iterate all blooms:
        for (int i = 1; i < points.length; i++){
            if (points[i][0] > end){
                arrows ++;
                end = points[i][1];
            }
        }

        return arrows;
    }
}
```

## Leetcode 435. 无重叠区间

#### 题目链接: [题目](https://leetcode.cn/problems/non-overlapping-intervals/)

#### 思路:
这道题就是和上道题的一个小改动，最后 return 的东西变了

```Java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        
        if (intervals == null || intervals.length == 0){
            return 0; 
        }
        // sorting: 
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));


        int count = 1;
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i ++){
            
            // lets see if the current start is overlapping the end:
            if (intervals[i][0] >= end){
                count ++;
                end = intervals[i][1];
            }
        }

        return intervals.length - count; 

    }
}
```

## Leetcode 763. 划分字母区间

#### 题目链接: [题目](https://leetcode.cn/problems/partition-labels/)

#### 思路：
这道题主要是 track 每个单词最后一个 placement。

```Java
class Solution {
    public List<Integer> partitionLabels(String s) {
        // track the last apprance of each character: 
        List<Integer> res = new ArrayList<>(); 

        int [] lastIndex = new int[26]; 
        for (int i = 0; i < s.length(); i ++){
            lastIndex[s.charAt(i) - 'a'] = i; 
        }

        int start = 0;
        int end = 0; 


        for (int i = 0; i < s.length(); i ++ ){
            end = Math.max(end, lastIndex[s.charAt(i) - 'a']); 

            if (i == end){
                res.add(end - start + 1); 
                start = i + 1;

            }
        }

        return res; 
    }
}
```

## 总结



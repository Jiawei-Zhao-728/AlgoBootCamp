# 代码随想录算法训练营第2天|  209.长度最小的子数组,  59.螺旋矩阵II, 开发商购买土地



## Leetcode  209: 长度最小的子数组

#### 题目链接： [题目](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

#### 思路

这道题的思路来说，一开始是写了两个 case，就是一定 R 是一个 case，然后移动 L 是一个 case，但是这样的话，在第一个 loop 结束之后，我们还要在检查一次 L，还要再去 increment L，所以这样子很麻烦。 所以最 optimal 的 solution 就是在大 loop 里面一直会 increment R，但是当 total 大于等于，我们就 increment L，这样子来保证我们得到最 optimal 的写法。

```Java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int total = 0, l = 0, r = 0;
        int res = Integer.MAX_VALUE;

        while (r < nums.length){
            total += nums[r];
            r ++;

            while (total >= target){
                res = Integer.min(res,  r- l);
                total -= nums[l];
                l += 1;
            }
        }
        if (res == Integer.MAX_VALUE){
            return 0;
        }else{
            return res;
        }
    }

}
```

## Leetcode 59: 螺旋矩阵II

#### 题目链接: [题目](https://leetcode.cn/problems/spiral-matrix-ii/)

#### 思路:
这道题主要是一个从外圈往内圈 decrement 的过程，所以把 variable decrement 好，其实问题不大。然后同时注意一下在转圈的时候，转角处容易 double count，会影响结果。 除此之外，其实没什么了。


```Java
class Solution {
    public int[][] generateMatrix(int n) {
        int left = 0, right = n - 1;
        int top = 0, buttom = n -1; 
        int [][] matrix = new int[n][n];
        int index = 1;

        // now we fill in:
        while (left <= right){
            // populate top:
            for (int i = left; i <= right; i ++){
                matrix[top][i] = index;
                index += 1;
            }

            for (int i = top + 1; i <= right; i ++){
                matrix[i][right] = index;
                index += 1;
            }

            for (int i = right - 1; i >= left; i --){
                matrix[buttom][i] = index;
                index += 1;
            }

            for (int i = buttom - 1; i >= top + 1; i --){
                matrix[i][left] = index;
                index += 1;
            }


            left ++;
            top ++;
            right --;
            buttom --;
        }

        return matrix;
    }
}
```

## 开发商购买土地

#### 题目链接: [题目](https://kamacoder.com/problempage.php?pid=1044)

#### 思路：
这道题其实最直接的做法就是最好，我们直接枚举所有的切法，然后找到 diff 最小的就好。

```Java
package 每日打卡.Day_2;
import java.util.Scanner;

public class Main {
    public static void main(String [] args){
        Scanner sc = new Scanner( System.in ); 
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] grid = new int[n][m];
        int total = 0;
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                grid[i][j] = sc.nextInt();
                total += grid[i][j];
            }
        }

        int minDiff = Integer.MAX_VALUE; 

        // 横切：
        int rowSum = 0; 
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j++){
                rowSum += grid[i][j];
            }
            int diff = Math.abs(total - 2 * rowSum);
            minDiff = Math.min(minDiff, diff); 
        }

        // 竖切：
        int colSum = 0;
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++){
                colSum += grid[i][j];
            }
            int diff = Math.abs(total - 2 * colSum);
            minDiff = Math.min(minDiff, diff);
        }

        System.out.println(minDiff);


    }
}
```

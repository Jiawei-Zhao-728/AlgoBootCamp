# 代码随想录算法训练营第 29 天| Leetcode 134. 加油站, Leetcode 135. 分发糖果, Leetcode 860. 柠檬水找零, Leetcode 406. 根据身高重建队列

## Leetcode 134. 加油站

#### 题目链接： [题目](https://leetcode.cn/problems/gas-station/)

#### 思路：

这道题，主要思路是，第一，如果 cost 和 大于 gas 和，那么就代表没有一个点可以绕圈一周。

第二，如果判断开始的话，我们如果但凡有个 current tank 是 小于 0，代表从哪个 start 到 current 都无法做 start，所以我们就从下一个开始。 

```Java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length; 

        int total_tank = 0; 
        int current_tank = 0;
        int start = 0; 

        for (int i = 0; i < n; i ++){
            int diff = gas[i] - cost[i]; 

            total_tank += diff;
            current_tank += diff; 

            if (current_tank < 0){
                start = i + 1;
                current_tank = 0;
            }
        }


        if (total_tank >= 0){
            return start;
        }else{
            return -1 ;
        }


    }
}
```

## Leetcode 135. 分发糖果

#### 题目链接: [题目](https://leetcode.cn/problems/candy/)

#### 思路:
这道题主要是有一个 two pass
```Java
class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length; 
        if (n == 0) return 0; 

        int [] candies = new int [n] ; 
        Arrays.fill(candies, 1);

        // first scan
        for (int i = 1; i < ratings.length; i ++){
            if (ratings[i] > ratings[i - 1]){
                candies[i] = candies[i - 1] + 1;
            }
        }

        // second scan: 
        for ( int i = ratings.length - 2; i >= 0; i --){
            if (ratings[i] > ratings[i + 1]){
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
        }

        int total = 0; 
        for (int candy : candies){
            total += candy;
        }

        return total; 
    }
}
```

## Leetcode 860. 柠檬水找零

#### 题目链接: [题目](https://leetcode.cn/problems/lemonade-change/)

#### 思路：

其实就是模拟

```Java
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0;
        int ten = 0; 

        for (int bill : bills){
            if (bill == 5){
                five += 1; 
            }else if (bill == 10){
                if (five == 0){
                    return false;
                }

                five -= 1;
                ten += 1;
            }else {
                if (five > 0 && ten > 0){
                    five --;
                    ten --; 
                } else if (five >= 3){
                    five -= 3; 
                } else {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Leetcode 406. 根据身高重建队列

#### 题目链接: [题目](https://leetcode.cn/problems/queue-reconstruction-by-height/)

#### 思路:

这道题主要是 sort

```Java
class Solution {
    public int[][] reconstructQueue(int[][] people) {

        //  = sorting
        Arrays.sort(people, (a, b) -> {
            if (a[0] != b[0]){
                return b[0] - a[0]; 
            }else{
                return a[1] - b[1];
            }
        });

        List <int[]> list = new ArrayList<>(); 
        for (int [] p : people) {
            list.add(p[1], p);

        }

        return list.toArray(new int[people.length][]);

    }
}
```

## 总结

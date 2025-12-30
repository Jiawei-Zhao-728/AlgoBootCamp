# 代码随想录算法训练营第 24 天| Leetcode 93. 复原 IP 地址, Leetcode 78. 子集, Leetcode 90. 子集 II

## Leetcode 93. 复原 IP 地址

#### 题目链接： [题目](https://leetcode.cn/problems/restore-ip-addresses/)

#### 思路：
这道题的本质是：在字符串中找3个切割点，把字符串分成4段。

想象你在处理一个字符串：

从开头开始：尝试截取1个、2个或3个字符作为第一段

检查是否合法：

截取的这一段是不是有效的IP段？

如果不是，放弃这个选择

如果合法：把这段加入路径，继续处理剩下的字符串

递归处理：对剩下的字符串重复这个过程

回溯：尝试完当前选择后，把它从路径中移除，尝试下一个选择

成功条件：当有4段且用完所有字符时，得到一个有效IP

```Java
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), res);

        return res; 
    }

    private void backtrack (String s, int start, List<String> path, List<String> res){
        // stopping condition 1:
        if (path.size() == 4){
            if (start == s.length()){
                res.add(String.join(".", path));
            }
            return;
        }
        // when not at the end 
        if (start == s.length()){
            return; 
        }

        for (int len = 1; len <= 3; len ++){

            if (len + start > s.length()){
                break;
            }

            String seg = s.substring(start, start + len); 

            if (isValide(seg)){
                path.add(seg);
                backtrack(s, start + len, path, res); 
                path.remove(path.size() - 1); 
            }


        }
    }

    private boolean isValide(String segnment){
        // check size: 
        if (segnment.length() > 3) return false; 

        // check for zero:
        if (segnment.length() > 1 && segnment.charAt(0) == '0') return false;

        int num = Integer.parseInt(segnment); 
        return (num >= 0 && num <= 255); 

    }
}
```

## Leetcode 78. 子集

#### 题目链接: [题目](https://leetcode.cn/problems/subsets/)

#### 思路:
这道题的核心思路就是要往前看，任何看过的 element 我们就不管了。

```Java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), res);

        return res;
    }

    private void backtrack (int [] nums, int start, List<Integer> path, List<List<Integer>> res){
        res.add(new ArrayList<>(path));

        for (int i = start; i < nums.length; i++){
            path.add(nums[i]);
            backtrack(nums, i + 1, path, res);
            path.remove(path.size() - 1);

        }
    }
}
```

## Leetcode 90. 子集 II

#### 题目链接: [题目](https://leetcode.cn/problems/subsets-ii/)

#### 思路：
这道题和上一题的区别就是我们要做一次去重。

```Java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);  // 关键：先排序
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;

    }

    private void backtrack (int[] nums, int start, List<Integer> path, List<List<Integer>> res){
        // adding every node: 
        res.add(new ArrayList<>(path)); 


        // iterate:
        for (int i = start; i < nums.length; i ++){
            // jump over duplicate
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }

            // 选择当前元素
            path.add(nums[i]);
            // 递归：从下一个位置开始
            backtrack(nums, i + 1, path, res);
            // 回溯
            path.remove(path.size() - 1);



        }
    }
}
```

## 总结




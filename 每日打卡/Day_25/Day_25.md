# 代码随想录算法训练营第 25 天| Leetcode 491. 递增子序列, Leetcode 46. 全排列, Leetcode 47. 全排列 II

## Leetcode 491. 递增子序列

#### 题目链接： [题目](https://leetcode.cn/problems/non-decreasing-subsequences/)

#### 思路：
这道题还是 backtracking，但是要注意同层去重，和保证一个变大性，每个数比之前的大。

```Java
class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> res = new ArrayList<>(); 
        backtrack(nums, 0, new ArrayList<>(), res);
        return res; 


    }

    private void backtrack (int[] nums, int start, List<Integer> path, List<List<Integer>> res){
        // more than two, we add
        if (path.size() >= 2){
            res.add(new ArrayList<>(path));
        }
        // used it to 去重
        Set<Integer> used = new HashSet<>(); 

        for (int i = start; i < nums.length; i ++){
            if (!path.isEmpty() && nums[i] < path.get(path.size() - 1)){
                continue;
            }

            if (used.contains(nums[i])){
                continue;
            }

            used.add(nums[i]);
            path.add(nums[i]); 
            backtrack(nums, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }
}
```

## Leetcode 46. 全排列

#### 题目链接: [题目](https://leetcode.cn/problems/permutations/)

#### 思路:

这道题主要是记住每次从 0 开始，没有 start。

```Java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>(); 
        boolean[] used = new boolean[nums.length];
        backtrack (nums, new ArrayList <> (), res, used);
        return res; 
        
    }

    private void backtrack (int [] nums, List<Integer> path, List<List<Integer>> res, boolean [] used){
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i ++){
            if (!used[i]) {
                used[i] = true; 
                path.add(nums[i]);

                // recurse: 
                backtrack(nums, path, res, used); 

                // backtrack: 
                path.remove(path.size() - 1); 
                used[i] = false; 


            }

        }



    }
}
```

## Leetcode 47. 全排列 II

#### 题目链接: [题目](https://leetcode.cn/problems/permutations-ii/)

#### 思路：

这里的关键条件是要去重

```Java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        boolean [] used = new boolean[nums.length];
        backtrack(nums, new ArrayList<>(), res, used);
        return res; 
        
        
    }

    private void backtrack (int [] nums, List<Integer> path, List<List<Integer>> res, boolean [] used){
        if (path.size() == nums.length){
            res.add(new ArrayList<>(path)); 
            return; 
        }

        for (int i = 0; i < nums.length; i ++ ) {
            // used
            if (used[i]){
                continue; 
            }

            // 关键去重条件：如果和前一个相同，且前一个没用过，跳过
            if (i > 0 && nums[i] == nums[i - 1] &&!used[i - 1]){
                continue; 
            }

            used[i] = true; 
            path.add(nums[i]); 

            backtrack(nums, path, res, used);

            path.remove(path.size() - 1);
            used[i] = false; 
        }
    }
}
```

## 总结

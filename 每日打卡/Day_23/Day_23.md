# 代码随想录算法训练营第 23 天| Leetcode 39. 组合总和, Leetcode 40. 组合总和 II, Leetcode 131. 分割回文串

## Leetcode 39. 组合总和

#### 题目链接： [题目](https://leetcode.cn/problems/combination-sum/)

#### 思路：

这道题，最关键的地方在我们怎么 iterate 这个 backtracking。和昨天的题目不一样，这次我们可以用同样的 element，所以，按道理来说，我们可以一直用同样的 element，但是为了避免重复的答案，我们不再看之前的 element，我们只 iterate 当前的，和 future 的。

```Java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>(); 
        Arrays.sort(candidates); 
        backtrack(candidates, target, 0, new ArrayList<>(), res, 0);
        return res; 
    }

    private void backtrack (int [] candidates, int target, 
    int start, 
    List<Integer> path, 
    List <List<Integer>> res,
    int sum
    ){
        
        // two stoping conditions
            // when success:
        if (sum == target){
            res.add(new ArrayList<>(path)); 
            return;
        }

            // when fail:
        if (sum > target){
            return; 
        }


        // iterate
        for (int i = start; i < candidates.length; i ++){
            // pruning if the current sum is larger than the target, then we just break; 
            if (sum + candidates[i] > target){
                break;
            }
            // backtrack: 
            path.add(candidates[i]); 
            backtrack(candidates, target, i, path, res, sum + candidates[i]); 
            path.remove(path.size() - 1); 

        }


    }
}
```

## Leetcode 40. 组合总和 II

#### 题目链接: [题目](https://leetcode.cn/problems/combination-sum-ii/)

#### 思路:

这道题很重要的一个点，是为了保证没有重复组合；在同一层递归中，如果当前数字和前一个数字相同，就跳过。

```Java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates); 

        backtrack(candidates, target, 0, new ArrayList<>(), res);

        return res; 
        


    }

    private void backtrack (int [] candidates, int target, int start, 
    List <Integer> path, List<List<Integer>> res
    ){
        // stoping condition:
        if (target == 0){
            res.add(new ArrayList<>(path)); 
            return;
        } 

        // iterate:
        for (int i = start; i < candidates.length; i++){
            if (candidates[i] > target){
                break;
            }

            // 跳过同一层的重复元素： 
            if (i > start && candidates[i] == candidates[i - 1]){
                continue;
            }

            path.add(candidates[i]);
            backtrack(candidates, target - candidates[i], i + 1, path, res);
            path.remove(path.size() -1); 
        }
    }
}
```

## Leetcode 131. 分割回文串

#### 题目链接: [题目](https://leetcode.cn/problems/palindrome-partitioning/)

#### 思路：

这道题，分两个部分，一个是判断回文，另一个是看怎么切：

从起点开始，尝试所有可能长度的子串

如果当前子串是回文，就加入路径，继续处理剩下的部分

处理完整个字符串后，把路径加入结果

```Java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), res);
        return res;
    }

    private boolean isPalidrome (String s, int l, int r){

        while (l < r){
            if (s.charAt(l) != s.charAt(r)){
                return false; 
            }
            l ++;
            r --; 
        }

        return true; 
    }

    private void backtrack (String s, int start, List<String>path, 
    List<List<String>> res)
    {
        // at the end: 
        if (start == s.length()){
            res.add(new ArrayList<>(path));
            return;
        }

        for (int end = start; end < s.length(); end ++){
            if (isPalidrome(s, start, end)){
                String subString = s.substring(start, end + 1); 
                path.add(subString);
                backtrack(s, end + 1, path, res);
                // 回溯
                path.remove(path.size() - 1);

            }
        }
    }
}
```

## 总结

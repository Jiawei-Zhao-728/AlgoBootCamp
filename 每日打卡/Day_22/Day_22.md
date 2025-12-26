# 代码随想录算法训练营第 22 天| 回溯算法 part01

## 理论基础

回溯算法在二叉树中已经接触过，现在正式开始回溯算法专题。建议先看视频，对回溯算法有个整体了解。

## Leetcode 77. 组合

#### 题目链接： [题目](https://leetcode.cn/problems/combinations/)

#### 思路：

**回溯算法三要素**：

1. **路径（path）**：已经做出的选择
2. **选择列表**：当前可以做的选择（从 `start` 到 `n`）
3. **结束条件**：路径长度达到 `k`

**核心思想**：

- 用 `start` 参数避免重复：每次从 `start` 开始选择，保证组合是递增的（如 [1,2] 不会出现 [2,1]）
- 回溯过程：**前进**（add）→ **探索**（递归）→ **回溯**（remove）

```Java

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(n, k, 1, new ArrayList<>(), res);
        return res;
    }

    private void backtrack (int n, int k, int start, List<Integer> path, List<List<Integer>> result){
        // if we choose to the kth number, then we added to the result:
        if (path.size()==k){
            result.add(new ArrayList<>(path));
            return;
        }

        // iterate:
        for (int i = start; i <= n; i++){
            path.add(i);
            backtrack(n, k, i+1, path, result);
            path.remove(path.size() - 1);
        }
    }
}

```

## Leetcode 216. 组合总和 III

#### 题目链接: [题目](https://leetcode.cn/problems/combination-sum-iii/)

#### 思路:

这道题和上一道题一样，但是改变了一下这个判断条件。

```Java
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List <List<Integer>> res = new ArrayList<>();
        backtrack(k, n, 1, new ArrayList<>(), res, 0);
        return res;
    }

    private void backtrack (int k, int n, int start,
    List<Integer> path, List<List<Integer>> res, int sum){

        if (path.size() == k && sum == n){
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i <= 9; i ++){
            path.add(i);
            sum += i;
            backtrack(k, n, i + 1, path, res, sum);
            sum -= i;
            path.remove(path.size() - 1);
        }
    }
}
```

## Leetcode 17. 电话号码的字母组合

#### 题目链接: [题目](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

#### 思路：

其实道理是一样的，但是我们要知道怎么去 iterate。

```Java
class Solution {
    private static final String[] KEYPAD = {
        "",
        "",
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();

        if (digits == null || digits.length() == 0){
            return result;
        }

        backtrack(digits, 0, new StringBuilder(), result);

        return result;
    }

    private void backtrack (String digits, int index, StringBuilder path, List<String> res){
        // add the finished variant to the result
        if (index == digits.length()){
            res.add(path.toString());
            return;
        }

        // get the digit pad we want:
        char digit = digits.charAt(index);
        String letter = KEYPAD[digit - '0'];

        // now we iterate:
        for (int i = 0; i < letter.length(); i++){
            path.append(letter.charAt(i));
            backtrack(digits, index + 1, path, res);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

## 总结

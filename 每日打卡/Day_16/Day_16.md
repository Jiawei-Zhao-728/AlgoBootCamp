# 代码随想录算法训练营第 16 天| Leetcode 513. 找树左下角的值, Leetcode 112. 路径总和, Leetcode 113. 路径总和 II, Leetcode 106. 从中序与后序遍历序列构造二叉树, Leetcode 105. 从前序与中序遍历序列构造二叉树

## Leetcode 513. 找树左下角的值

#### 题目链接： [题目](https://leetcode.cn/problems/find-bottom-left-tree-value/)

#### 思路：

这道题，我们就是用 BFS，然后每到一层，我们就更新那一层的第一个 node。

```Java
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        // this question, since we need to know the most left of the buttom, we use BFS:
        Queue <TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int result = 0;

        // bfs
        while (!queue.isEmpty()){
            int queuelen = queue.size();

            for (int i = 0; i < queuelen; i++){
                TreeNode poped = queue.poll();
                if (i == 0){
                    result = poped.val;
                }

                if(poped.left != null) queue.offer(poped.left);
                if(poped.right != null) queue.offer(poped.right);
            }

        }

        return result;

    }
}
```

## Leetcode 112. 路径总和

#### 题目链接: [题目](https://leetcode.cn/problems/path-sum/)

#### 思路:

```Java

class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        boolean res = dfs(root, 0, targetSum);
        return res;
    }

    private boolean dfs (TreeNode node, int cursum, int targetSum) {
        // base case: when hit the leaf node:
        cursum += node.val;
        if (node.left == null && node.right == null){
            return cursum == targetSum;
        }

        boolean left = false, right = false;
        if (node.left != null){
            left = dfs(node.left, cursum, targetSum);
        }
        if (node.right != null){
            right = dfs(node.right, cursum, targetSum);
        }

        return left || right;
    }
}
```

## Leetcode 113. 路径总和 II

#### 题目链接: [题目](https://leetcode.cn/problems/path-sum-ii/)

#### 思路：

Path Sum I 只需要判断是否存在满足条件的路径，所以用一个 int 变量记录当前路径和就够了。Path Sum II 需要返回所有满足条件的完整路径，所以必须用 List 记录走过的每个节点。
int 是值传递，每一层递归都有自己的副本，返回上一层时自动恢复，不需要手动处理。List 是引用传递，所有递归层共享同一个 List，所以进入节点时 add，离开节点时必须 remove，这就是回溯。
回溯的本质是"恢复现场"：探索完一条路后，把状态还原到探索之前，才能正确探索下一条路。
另外，找到满足条件的路径时，要用 new ArrayList<>(path) 复制一份再存入结果，否则存的是引用，后续回溯会把已存的结果也清空。

```Java

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List <List<Integer>> res = new ArrayList<>();
        List <Integer> cur = new ArrayList<>();
        if(root == null) return res;
        dfs(root, targetSum, cur, 0, res);
        return res;

    }

    private void dfs (TreeNode node, int targetSum, List<Integer> curPath, int curSum, List<List<Integer>> res) {
        // add current node to path and sum:
        curPath.add(node.val);
        curSum += node.val;
        // base case: if at leaf node
        if (node.left == null && node.right == null){
            if (targetSum == curSum){
                res.add(new ArrayList<>(curPath));
            }
        }

        if (node.left != null) {
            dfs(node.left, targetSum, curPath, curSum, res);
        }
        if (node.right != null){
            dfs(node.right, targetSum, curPath, curSum, res);
        }

        curPath.remove(curPath.size() -1 );


    }
}
```

## Leetcode 106. 从中序与后序遍历序列构造二叉树

#### 题目链接: [题目](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## 核心知识：遍历顺序

```
中序 (Inorder):   左 → 根 → 右
后序 (Postorder): 左 → 右 → 根
```

## 关键洞察

```
postorder: [9, 15, 7, 20, 3]
                         ↑
                      最后一个一定是根！

inorder:   [9, 3, 15, 20, 7]
               ↑
            找到根的位置，左边是左子树，右边是右子树
```

## 图解过程

### 第一步：找根节点

`postorder` 最后一个 = 3，这是根。在 `inorder` 中找到 3 的位置：

```
inorder:   [9] | 3 | [15, 20, 7]
            ↑       ↑
          左子树    右子树
```

### 第二步：理解为什么倒着取是"根 → 右 → 左"

```
postorder: [9, 15, 7, 20, 3]
                    ↑
        因为后序是 左→右→根，倒着就是 根→右→左
        所以取完根后，下一个是右子树的根！
```

### 第三步：递归处理

- 右子树 `inorder: [15, 20, 7]`，根是 20
- 左子树 `inorder: [9]`，根是 9

## 为什么要先建右子树？

```
postorder: [9, 15, 7, 20, 3]
            ↑   ↑   ↑   ↑   ↑
            左  ---右---  根

倒着取: 3(根) → 20(右子树根) → 7 → 15 → 9(左子树)
```

如果先建左子树，`postIndex` 会指向错误的节点！

```Java

class Solution {
    int postIndex;
    Map<Integer, Integer> inorderMap = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // get the head:
        postIndex = postorder.length - 1;

        // populate the inorderMap
        for (int i = 0; i < inorder.length; i ++ ){
            inorderMap.put(inorder[i], i);
        }

        return build(postorder, 0, inorder.length - 1);

    }

    private TreeNode build (int[] postorder, int left, int right){
        if (left > right) return null;

        int rootVal = postorder[postIndex--];
        TreeNode root = new TreeNode(rootVal);

        // 在中序找到根的位置：
        int mid = inorderMap.get(rootVal);

        root.right = build(postorder, mid + 1, right);
        root.left = build(postorder, left, mid - 1);

        return root;
    }
}
```

## Leetcode 105. 从前序与中序遍历序列构造二叉树

#### 题目链接: [题目](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

#### 思路:

1. 找根：前序第一个 / 后序最后一个
2. 分左右：在中序中找根的位置
3. 递归建树

唯一区别就是取的方向决定了建树顺序：  
前序 根 → 左 → 右 → preIndex++ → 先建左子树  
后序 左 → 右 → 根 → postIndex-- → 先建右子树

```Java

class Solution {
    int preIndex = 0;
    Map <Integer, Integer> inorderMap = new HashMap<>();


    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < preorder.length; i ++ ){
            inorderMap.put(inorder[i], i);
        }

        return build(preorder, 0, inorder.length - 1);

    }

    private TreeNode build (int[] preorder, int left, int right){
        if (left > right) return null;

        int rootVal = preorder[preIndex ++];
        TreeNode root = new TreeNode(rootVal);

        int mid = inorderMap.get(rootVal);

        root.left = build(preorder, left, mid - 1);
        root.right = build(preorder, mid + 1, right);

        return root;

    }
}
```

## 总结

### 核心技巧

- **513 找树左下角的值**：BFS 层序遍历，每层第一个节点就是该层最左节点
- **112 路径总和**：DFS + 值传递（int），不需要回溯，判断是否存在即可
- **113 路径总和 II**：DFS + **回溯**（List 引用传递），必须 `add` 后 `remove`，找到路径时用 `new ArrayList<>(path)` 复制
- **106 后序+中序构造**：后序最后一个 = 根，倒着取（`postIndex--`），**先建右子树**
- **105 前序+中序构造**：前序第一个 = 根，正着取（`preIndex++`），**先建左子树**

### 关键对比

- **值传递 vs 引用传递**：int 自动恢复，List 需要手动回溯
- **前序 vs 后序构造**：取根的方向决定建树顺序（前序先左，后序先右）

### 一句话

今天重点是**回溯的应用**（113）和**遍历序列构造二叉树**（105/106），理解引用传递需要回溯，值传递不需要。

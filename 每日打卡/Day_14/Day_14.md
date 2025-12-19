# 代码随想录算法训练营第 14 天| Leetcode 226. 翻转二叉树, Leetcode 101. 对称二叉树, Leetcode 104. 二叉树的最大深度, Leetcode 111. 二叉树的最小深度

## Leetcode 226. 翻转二叉树（优先掌握递归）

#### 题目链接： [题目](https://leetcode.cn/problems/invert-binary-tree/)

#### 思路：

翻转二叉树：交换每个节点的左右子树

**递归方法（后序遍历）**：

1. 确定递归函数参数和返回值：`TreeNode invertTree(TreeNode root)`
2. 确定终止条件：`if (root == null) return null;`
3. 确定单层递归逻辑：
   - 先递归翻转左子树
   - 再递归翻转右子树
   - 最后交换当前节点的左右子树

**遍历顺序**：后序遍历（先处理左右子树，再处理根）

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode l = invertTree(root.left);
        TreeNode r = invertTree(root.right);

        root.left = r;
        root.right = l;

        return root;
    }
}
```

## Leetcode 101. 对称二叉树（优先掌握递归）

#### 题目链接: [题目](https://leetcode.cn/problems/symmetric-tree/)

#### 思路:

判断二叉树是否对称：比较左右子树是否镜像

**递归方法**：

1. 确定递归函数参数：需要同时比较两个节点 `isMirror(TreeNode l, TreeNode r)`
2. 确定终止条件：
   - 两个都为空 → `true`
   - 一个为空一个不为空 → `false`
   - 两个值不相等 → `false`
3. 确定单层递归逻辑：
   - 比较 `l.left` 和 `r.right`（外侧）
   - 比较 `l.right` 和 `r.left`（内侧）
   - 都对称才返回 `true`

**关键点**：同时比较两个节点，而不是单个节点递归

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isMirror(root.left, root.right);
    }

    private boolean isMirror (TreeNode l, TreeNode r){
        // base case:
        if (l == null && r == null) return true;
        if (l == null || r == null) return false;

        if (l.val != r.val) return false;

        return isMirror(l.left, r.right) && isMirror(r.left, l.right);
    }
}
```

## Leetcode 104. 二叉树的最大深度（优先掌握递归）

#### 题目链接: [题目](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

#### 思路：

**深度 vs 高度**：

- **深度**：从根节点到该节点的路径长度（从上往下）
- **高度**：从该节点到叶子节点的最长路径长度（从下往上）
- 根节点的深度 = 1，根节点的高度 = 树的高度

**递归方法（后序遍历）**：

1. 确定递归函数参数和返回值：`int maxDepth(TreeNode root)`，返回以 root 为根节点的树的最大深度
2. 确定终止条件：`if (root == null) return 0;`（空节点深度为 0）
3. 确定单层递归逻辑：
   - 左子树最大深度：`maxDepth(root.left)`
   - 右子树最大深度：`maxDepth(root.right)`
   - 当前节点深度：`1 + max(左深度, 右深度)`

**为什么用后序遍历？** 需要先知道左右子树的深度，才能计算当前节点的深度

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        int l = maxDepth(root.left);
        int r = maxDepth(root.right);

        return 1 + Math.max(l, r);
    }
}
```

## Leetcode 111. 二叉树的最小深度（优先掌握递归）

#### 题目链接: [题目](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

#### 思路:

**最小深度 vs 最大深度的区别**：

- **最大深度**：`1 + max(左深度, 右深度)`（即使一边为 null，另一边也有深度）
- **最小深度**：必须到达**叶子节点**，不能直接用 `min`！

**关键坑点**：当一边子树为 null 时：

- 如果 `root.left == null`，最小深度 = `1 + 右子树最小深度`（不能走左子树）
- 如果 `root.right == null`，最小深度 = `1 + 左子树最小深度`（不能走右子树）
- 如果两边都不为 null，最小深度 = `1 + min(左深度, 右深度)`

**递归方法（后序遍历）**：

1. 确定递归函数参数和返回值：`int minDepth(TreeNode root)`
2. 确定终止条件：`if (root == null) return 0;`
3. 确定单层递归逻辑：
   - 先递归求左右子树最小深度
   - **判断单边为 null 的情况**（关键！）
   - 都不为 null 才用 `min`

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public int minDepth(TreeNode root) {
        if (root == null)return 0;

        int l = minDepth(root.left);
        int r = minDepth(root.right);

        // 最重要的两行逻辑，就是当 r 没有的时候 长度是 l + 1。 反过来也是一样。
        if (root.right == null) return 1 + l;
        if (root.left == null) return 1 + r;
        return 1 + Math.min(l, r);
    }
}
```

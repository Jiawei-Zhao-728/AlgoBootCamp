# 代码随想录算法训练营第 15 天| Leetcode 110. 平衡二叉树, Leetcode 257. 二叉树的所有路径, Leetcode 404. 左叶子之和, Leetcode 222. 完全二叉树的节点个数

## Leetcode 110. 平衡二叉树（优先掌握递归）

#### 题目链接： [题目](https://leetcode.cn/problems/balanced-binary-tree/)

#### 思路：

**平衡二叉树定义**：每个节点的左右两个子树的高度差的绝对值不超过 1

**递归方法（后序遍历）**：

1. 确定递归函数参数和返回值：`int getheight(TreeNode node)`，返回节点高度，如果返回 -1 表示不平衡
2. 确定终止条件：`if (node == null) return 0;`（空节点高度为 0）
3. 确定单层递归逻辑：
   - 递归求左子树高度，如果为 -1 直接返回 -1（不平衡）
   - 递归求右子树高度，如果为 -1 直接返回 -1（不平衡）
   - 判断左右高度差：`if (Math.abs(l - r) > 1) return -1;`
   - 返回当前节点高度：`1 + max(左高度, 右高度)`

**为什么用 -1 作为标记？**

- 正常高度 ≥ 0，用 -1 表示"不平衡"状态
- 可以在递归过程中**提前终止**，一旦发现不平衡就向上传递 -1
- 最后判断：`getheight(root) != -1` 即可

**高度 vs 深度（巩固）**：

- 这里计算的是**高度**（从下往上），因为需要从叶子节点向上累加
- 后序遍历：先知道左右子树高度，才能判断当前节点是否平衡

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public boolean isBalanced(TreeNode root) {
        return getheight(root) != -1;
    }

    // since we need to keep track of height, we want a new recursive function:
    public int getheight(TreeNode node){
        // when hit the buttom
        if (node == null){
            return 0;
        }

        int l = getheight(node.left);
        int r = getheight(node.right);

        if (l == -1) return -1;
        if (r == -1) return -1;

        if (Math.abs(l - r) > 1) return -1;

        // Here we get the height of the current node:
        return 1 + Math.max(l, r);
    }
}
```

## Leetcode 257. 二叉树的所有路径（优先掌握递归）

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-paths/)

#### 思路:

**DFS + 路径记录**

1. **递归函数**：`getPath(TreeNode node, String path, List<String> allPath)`

   - `node`：当前节点
   - `path`：当前路径（String，不可变）
   - `allPath`：存储所有路径的结果列表

2. **处理当前节点**：`path += node.val`，把当前节点值加入路径

3. **终止条件**：到达叶子节点（`left == null && right == null`），把完整路径加入结果并返回

4. **递归左右子树**：
   - 如果左子树不为空：`getPath(node.left, path + "->", allPath)`
   - 如果右子树不为空：`getPath(node.right, path + "->", allPath)`
   - 注意：传入的是 `path + "->"`，创建新字符串，不影响原 path

**为什么不需要回溯？**

- String 是不可变的，每次 `path + "->"` 都创建新对象
- 递归返回时，上一层的 path 保持不变，自动"恢复"状态

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        getPath(root, "", res);;
        return res;
    }

    private void getPath (TreeNode node, String path, List<String> allPath) {

        path += node.val;

        if (node.left == null && node.right == null){
            allPath.add(path);
            return;
        }

        if (node.left != null) {
            getPath(node.left, path + "->", allPath);
        }
        if (node.right != null) {
            getPath(node.right, path + "->", allPath);
        }


    }
}
```

## Leetcode 404. 左叶子之和（优先掌握递归）

#### 题目链接: [题目](https://leetcode.cn/problems/sum-of-left-leaves/)

#### 思路：

这道题其实就是通过 dfs，每个节点 check 一下，有没有 left leaf，有的话，就加进去。

```Java

class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        // we use dfs:
        if (root == null) return 0;

        int sum = 0;

        // check if is left leaf:
        if (root.left != null && root.left.left == null && root.left.right == null) {
            sum += root.left.val;
        }

        sum += sumOfLeftLeaves(root.left);
        sum += sumOfLeftLeaves(root.right);

        return sum;
    }


}
```

## Leetcode 222. 完全二叉树的节点个数（优先掌握递归）

#### 题目链接: [题目](https://leetcode.cn/problems/count-complete-tree-nodes/)

#### 思路:

**递归方法（后序遍历）**：

1. **终止条件**：`if (root == null) return 0;`（空节点返回 0）

2. **单层递归逻辑**：
   - 当前节点：`node = 1`（当前节点本身）
   - 左子树节点数：`countNodes(root.left)`
   - 右子树节点数：`countNodes(root.right)`
   - 返回：`1 + 左子树节点数 + 右子树节点数`

**思路**：当前节点（1 个）+ 左子树节点数 + 右子树节点数

**注意**：这是普通二叉树的通用方法，完全二叉树可以用更优的方法（利用完全二叉树性质），但递归方法更通用

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java

class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;

        int node = 0;

        if (root != null){
            node += 1;
        }

        node += countNodes(root.left);
        node += countNodes(root.right);

        return node;
    }
}
```

## 总结

### 核心技巧

- **110 平衡二叉树**：用 -1 标记不平衡状态，计算高度的同时判断平衡性
- **257 二叉树的所有路径**：DFS + String 路径记录，String 不可变所以不需要回溯
- **404 左叶子之和**：判断左叶子：`node.left != null && node.left.left == null && node.left.right == null`
- **222 完全二叉树的节点个数**：递归 = 1 + 左子树节点数 + 右子树节点数

### 一句话

今天主要是**递归的灵活应用**，注意区分高度和深度，理解路径收集的思路。

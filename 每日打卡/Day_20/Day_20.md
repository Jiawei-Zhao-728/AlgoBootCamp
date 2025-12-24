# 代码随想录算法训练营第 20 天| Leetcode 235. 二叉搜索树的最近公共祖先, Leetcode 701. 二叉搜索树中的插入操作, Leetcode 450. 删除二叉搜索树中的节点

## Leetcode 235. 二叉搜索树的最近公共祖先

#### 题目链接： [题目](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

#### 思路：

这道题我们可以用到 bst 的特性，也就是说，我们可以有两个 val 之后，知道啊一个 node 的数字是两个 val 之间的，那么这个就是他们的中间。

```Java

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p, q);
    }

    private TreeNode dfs (TreeNode node, TreeNode p, TreeNode q){
        int minval = Math.min(p.val, q.val);
        int maxval = Math.max(p.val, q.val);

        TreeNode curr = node;

        while (curr != null){
            if (curr.val < minval){
                curr = curr.right;
            }else if (curr.val > maxval){
                curr = curr.left;
            }else{
                return curr;
            }
        }

        return null;


    }
}
```

## Leetcode 701. 二叉搜索树中的插入操作

#### 题目链接: [题目](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

#### 思路:

这道题最有趣的就是他们怎么 connect 这个新 node 和这个 leaf node 的，因为这次我想用递归来写。所有一个很重要的点就是，我们递下去，创建了 new node，然后在归的第一次，我们就 connect 了。

```Java

class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);

        if (val > root.val){
            root.right = insertIntoBST(root.right, val);
        }else{
            root.left = insertIntoBST(root.left, val);
        }

        return root;
    }
}
```

## Leetcode 450. 删除二叉搜索树中的节点

#### 题目链接: [题目](https://leetcode.cn/problems/delete-node-in-a-bst/)

#### 思路：

**BST 删除节点的三种情况**：

1. **要删除的节点是叶子节点**（左右都为空）

   - 直接返回 `null`（被包含在情况 2 或 3 中）

2. **要删除的节点只有一个子节点**

   - 左子树为空：返回右子树 `return root.right`
   - 右子树为空：返回左子树 `return root.left`
   - **关键**：用子节点替换当前节点

3. **要删除的节点有两个子节点**（最复杂）
   - 找到**右子树的最小值**（或左子树的最大值）
   - 用这个最小值**替换**当前节点的值
   - **删除**右子树中的这个最小值节点
   - **为什么用右子树最小值？** 它比左子树所有节点大，比右子树其他节点小，替换后仍保持 BST 性质

**递归逻辑**：

- 如果 `key < root.val`：递归删除左子树，`root.left = deleteNode(root.left, key)`
- 如果 `key > root.val`：递归删除右子树，`root.right = deleteNode(root.right, key)`
- 如果 `key == root.val`：按上述三种情况处理

**关键理解**：

- `root.left = deleteNode(...)` 和 `root.right = deleteNode(...)` 的作用是**连接**删除后的子树
- 删除节点后，需要把新的子树结构**连接回父节点**

**重点理解 `root.right = deleteNode(root.right, minNode.val);`**：

```Java
// 情况 3：有两个子节点
TreeNode minNode = findmin(root.right);  // 1. 找到右子树最小值节点
root.val = minNode.val;                  // 2. 用最小值替换当前节点值
root.right = deleteNode(root.right, minNode.val);  // 3. 删除右子树中的最小值节点
```

**为什么需要这一步？**

1. **我们已经替换了值**：`root.val = minNode.val`，当前节点的值已经变成最小值了
2. **但原最小值节点还在**：右子树中原来的 `minNode` 节点还在，需要删除它
3. **删除后需要重新连接**：删除 `minNode` 后，右子树的结构可能改变（比如 minNode 有右子树），需要把新的右子树结构连接回来

**例子**：

```
删除节点 5：
    5                   5 (值变成 6)
   / \                 / \
  3   7    → 替换后    3   7
     / \                 / \
    6   8               6   8
                        ↑
                    需要删除这个 6

删除 6 后：
    5 (值变成 6)
   / \
  3   7
       \
        8

root.right = deleteNode(root.right, 6) 的作用：
- 在右子树中删除值为 6 的节点
- 删除后返回新的右子树根节点（可能是 7，或者 7 的某个子节点）
- 用 root.right = 把这个新子树连接回来
```

**递归的巧妙之处**：

- `deleteNode(root.right, minNode.val)` 会在右子树中递归找到并删除 minNode
- 删除后返回新的右子树根节点
- `root.right =` 把这个新根节点连接回当前节点
- 这样整个树的结构就正确了

时间复杂度：O(h)，h 为树高
空间复杂度：O(h)，递归栈深度

```Java

class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val){
            root.left = deleteNode(root.left, key);
        } else if (key > root.val){
            root.right = deleteNode(root.right, key);
        }else{
            // we found it:
            if (root.left == null){
                return root.right;
            } else if (root.right == null){
                return root.left;
            }else{
                // when the node we want to delete has both child:
                TreeNode minNode = findmin(root.right);
                root.val = minNode.val;
                root.right = deleteNode(root.right, minNode.val);
            }
        }

        return root;
    }

    private TreeNode findmin (TreeNode node){
        while (node.left != null){
            node = node.left;
        }
        return node;
    }
}
```

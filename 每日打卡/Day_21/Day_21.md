# 代码随想录算法训练营第 21 天| Leetcode 669. 修剪二叉搜索树, Leetcode 108. 将有序数组转换为二叉搜索树, Leetcode 538. 把二叉搜索树转换为累加树

## Leetcode 669. 修剪二叉搜索树

#### 题目链接： [题目](https://leetcode.cn/problems/trim-a-binary-search-tree/)

#### 思路：

这道题的主要思路是如果我们遇到了在范围外的，比如说遇到比 high 大的，那么我们就看这个 node 的 left sub tree。 同理如果遇到比小的，那么就看 right sub tree，如果是在范围内的，我们就继续往下 trim。

```Java

class Solution {
    public TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) return null;

        if (root.val > high){
            return trimBST(root.left, low, high);
        }

        if (root.val < low) {
            return trimBST(root.right, low, high);
        }

        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);

        return root;
    }
}
```

## Leetcode 108. 将有序数组转换为二叉搜索树

#### 题目链接: [题目](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)

#### 思路:

这里就是用递归，每次我们会用中数去 create 一个 node，然后中数中数这个 node 会有 left 和 right children，这时候我们再把两边切割的 Array 给左边和右边。这样我们一直递归下去，我们就做好了这个 tree。

```Java

class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return buildTree(nums, 0, nums.length - 1);
    }

    private TreeNode buildTree (int[] nums, int left, int right){
        if (left > right){
            return null;
        }

        // find mid:
        int mid = left + (right - left) / 2;

        TreeNode root = new TreeNode(nums[mid]);

        root.left = buildTree(nums, left, mid - 1);
        root.right = buildTree(nums, mid + 1, right);

        return root;
    }
}
```

## Leetcode 538. 把二叉搜索树转换为累加树

#### 题目链接: [题目](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

#### 思路：

**累加树定义**：每个节点的值 = 原节点值 + 所有大于它的节点值之和

**核心思想：反向中序遍历 + 累加和**

**为什么用反向中序遍历（右 → 根 → 左）？**

- BST 中序遍历（左 → 根 → 右）是**递增序列**：从小到大
- 反向中序遍历（右 → 根 → 左）是**递减序列**：从大到小
- 累加树需要：**从大到小**累加，先处理大的，再处理小的

**累加逻辑**：

1. 先递归处理右子树（所有大于当前节点的值）
2. 累加当前节点：`sum += root.val`
3. 更新当前节点值：`root.val = sum`（此时 sum 是所有 >= 当前节点值的和）
4. 再递归处理左子树（所有小于当前节点的值）

**和 530、501 的双指针思路类似**：

- 都是利用 BST 中序遍历的有序性
- 530：用 `prev` 记录上一个节点，计算差值
- 538：用 `sum` 累加所有已访问的节点值

**例子**：

```
原 BST:       累加树:
    5             18
   / \           /  \
  2   13    →   20   13
     /  \           /  \
    7    15        21   15

反向中序遍历：15 → 13 → 7 → 5 → 2
累加过程：
  15: sum = 15, 15.val = 15
  13: sum = 28, 13.val = 28
  7:  sum = 35, 7.val = 35
  5:  sum = 40, 5.val = 40
  2:  sum = 42, 2.val = 42
```

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度

```Java

class Solution {
    private int sum = 0;
    public TreeNode convertBST(TreeNode root) {
        if (root == null) return null;

        // 反向中序遍历：右 → 根 → 左
        convertBST(root.right);

        sum += root.val;
        root.val = sum;

        convertBST(root.left);

        return root;
    }
}
```

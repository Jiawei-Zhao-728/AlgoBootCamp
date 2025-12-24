# 代码随想录算法训练营第 17 天| Leetcode 654. 最大二叉树, Leetcode 617. 合并二叉树, Leetcode 700. 二叉搜索树中的搜索, Leetcode 98. 验证二叉搜索树

## Leetcode 654. 最大二叉树

#### 题目链接： [题目](https://leetcode.cn/problems/maximum-binary-tree/)

#### 思路：

这道题的核心是递归构造最大二叉树，每次在当前数组范围内找到最大值，这个最大值就是当前的根节点。最大值左边所有的元素构造左子树，右边的所有元素构成右子树，然后随州两边分别递归执行同样操作。

递归的 base case 就是当 left > right 返回 null，表示这个范围内没有元素了。诶蹭递归做的事儿就是找到最大 index，然后创建根节点。递归处理左右两边

```Java

class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build (int[]nums, int left, int right){
        if (left > right) return null;

        // we find the max index in this section of the array:
        // which would be the root:
        int MaxIndex = left;
        for (int i = left; i <= right; i ++){
            if (nums[i] > nums[MaxIndex]){
                MaxIndex = i;
            }
        }

        // make the root:
        TreeNode root = new TreeNode(nums[MaxIndex]);

        // recurse the function:
        root.left = build(nums, left, MaxIndex - 1 );
        root.right = build(nums, MaxIndex + 1, right);

        return root;
    }
}
```

## Leetcode 617. 合并二叉树

#### 题目链接: [题目](https://leetcode.cn/problems/merge-two-binary-trees/)

#### 思路:

这道题其实是考虑到几种情况，第一是如果梁斌都没有，都是 null，那么我们也会返回 null。如果其中一个不是 null，我们就返回那个。如果两个都是有 node 的，我们就相加。  
同时。recursion 的关系是，我们两边同时看，这样子就是每次看的 position 都是一样的。每一层递归负责合并"对应位置"的两个节点，然后把左右子树的合并任务交给下一层递归。

```Java

class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null){
            // when both are null
            return null;
        }else if (root1 == null){
            // when one of them is not null
            return root2;
        }else if (root2 == null){
            return root1;
        }else{
            // when both are not null
            root1.val += root2.val;
            root1.left = mergeTrees(root1.left, root2.left);
            root1.right = mergeTrees(root1.right, root2.right);
            return root1;
        }
    }
}
```

## Leetcode 700. 二叉搜索树中的搜索

#### 题目链接: [题目](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

#### 思路：

**BST 特性**：左子树所有节点 < 根 < 右子树所有节点

**递归过程**：

1. **从上往下**：根据 BST 特性，如果 `root.val > val`，去左子树找；如果 `root.val < val`，去右子树找
2. **从下往上返回**：
   - 如果找到目标（`root.val == val`），直接返回该节点
   - 如果到达 null，返回 null
   - **关键**：递归调用的返回值会一层层向上传递，最终返回到最顶层

**递归返回机制理解**：

```
searchBST(3, 2)
  → searchBST(2, 2)  // 找到，返回节点 2
    ← 返回节点 2      // 从下往上返回
  ← 返回节点 2       // 继续向上传递
```

**代码逻辑**：

- `root = searchBST(root.left, val)`：把递归返回的结果赋给 root
- 如果找到，返回的就是目标节点；如果没找到，返回 null
- 最后 `return root` 把结果继续向上传递

**递归的本质 = 栈（Stack）**：

- 每次递归调用，系统会在**函数调用栈**中压入一个新的函数调用
- **后进先出（LIFO）**：最后调用的函数最先返回
- **从下往上返回**：栈顶的函数先返回，然后栈中的函数依次返回
- 这就是为什么递归的空间复杂度是 O(h)，因为栈的深度 = 树的高度

**递归 vs 迭代**：

- 递归：隐式使用系统栈
- 迭代：显式使用 `Stack<TreeNode>` 来模拟递归过程

时间复杂度：O(h)，h 为树高，BST 最坏情况 O(n)
空间复杂度：O(h)，递归栈深度

```Java
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) return null;

        if (root.val == val){
            return root;
        }else if (root.val > val){
            root = searchBST(root.left, val);
        }else {
            root = searchBST(root.right, val);
        }

        return root;


    }
}
```

## Leetcode 98. 验证二叉搜索树

#### 题目链接: [题目](https://leetcode.cn/problems/validate-binary-search-tree/)

#### 思路:

这道题的思路，我觉得应该是，每一个 leaf node，或者说每一个 node，其实都有一个最大可以是的值和最小可以是的值，有一个范围，那么我们每次 recurse 我们会 pass in 这个范围，然后通过范围来 verify 是否正确

```Java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate (TreeNode root, long min, long max){
        // base case:
        if (root == null) return true;

        if (root.val >= max || root.val <= min) return false;


        // recurse:
        boolean v1 = validate(root.left, min, root.val);
        boolean v2 = validate(root.right, root.val, max);

        return v1 && v2;
    }
}
```

## 总结

### 核心技巧

- **654 最大二叉树**：构造二叉树，前序遍历。每次找最大值作为根，递归构造左右子树
- **617 合并二叉树**：同时操作两个二叉树，考虑四种情况（都空、一个空、都不空），递归合并对应位置
- **700 二叉搜索树中的搜索**：利用 BST 特性（左小右大）剪枝，递归返回机制（从下往上返回）
- **98 验证二叉搜索树**：每个节点都要在范围内（min, max），传递上下界；或中序遍历检查是否递增

### 关键理解

- **递归 = 栈**：递归本质是函数调用栈，后进先出，从下往上返回
- **BST 特性**：左子树 < 根 < 右子树，中序遍历是递增序列
- **构造二叉树**：通常用前序遍历（先建根，再建左右）

### 一句话

今天重点是**BST 的特性应用**和**同时操作多个二叉树**，理解递归的栈本质很重要。

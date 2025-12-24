# 代码随想录算法训练营第 18 天| Leetcode 530. 二叉搜索树的最小绝对差, Leetcode 501. 二叉搜索树中的众数, Leetcode 236. 二叉树的最近公共祖先

## Leetcode 530. 二叉搜索树的最小绝对差

#### 题目链接： [题目](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

#### 思路：

**BST 中序遍历 + 双指针**

**核心思想**：

- BST 的中序遍历是**递增序列**
- 最小绝对差一定出现在**相邻节点**之间（因为序列是递增的）
- 用 `prev` 记录上一个节点，`node` 是当前节点，计算 `node.val - prev`

**双指针操作**：

1. **中序遍历**：左 → 根 → 右，保证访问顺序是递增的
2. **prev 指针**：记录上一个访问的节点值
3. **计算差值**：`if (prev != null) mindiff = Math.min(mindiff, node.val - prev)`
4. **更新 prev**：`prev = node.val`，为下一次比较做准备

**为什么操作要在 `inorder(left)` 和 `inorder(right)` 之间？**

中序遍历的顺序是：**左 → 根 → 右**

```
inorder(node.left);   // 1. 先访问左子树（所有左子树节点）
// 处理当前节点        // 2. 处理根节点（在这里！）
inorder(node.right);  // 3. 再访问右子树（所有右子树节点）
```

**关键理解**：

- 当执行到中间部分时，**左子树的所有节点都已经访问完了**
- 此时 `prev` 已经更新到**左子树的最大值**（也就是当前节点的前驱）
- 可以比较：`当前节点（根）` 和 `prev（左子树最大值）`
- 然后更新 `prev = 当前节点值`
- 接着访问右子树时，`prev` 就是当前节点，可以比较 `右子树的最小值` 和 `当前节点`

**例子**：

```
    5
   / \
  3   7
 / \
1   4

中序遍历：1 → 3 → 4 → 5 → 7
          ↑   ↑   ↑   ↑   ↑
         prev 当前 prev 当前 prev
```

所以操作必须在中间，才能保证访问顺序是递增的！

**为什么用中序遍历？**

- BST 中序遍历是递增序列，相邻节点差值最小
- 如果不用中序遍历，需要比较所有节点对，复杂度 O(n²)

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度

```Java

class Solution {
    // in order traversal
    private int mindiff = Integer.MAX_VALUE;
    private Integer prev = null;


    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return mindiff;
    }

    private void inorder (TreeNode node) {
        if (node == null) return;

        // left subtree;
        inorder(node.left);

        if (prev != null){
            mindiff = Math.min(mindiff, node.val - prev);
        }
        prev = node.val;

        inorder(node.right);
    }
}
```

## Leetcode 501. 二叉搜索树中的众数

#### 题目链接: [题目](https://leetcode.cn/problems/find-mode-in-binary-search-tree/)

#### 思路:
这道题还是同样的中序解法，BST 的中序解法可以升序去 iterate 所有的值，这样子，我们可以判断所有数。
```Java

class Solution {
    private List<Integer> modes; 
    private int currentVal; 
    private int currentCount;
    private int maxCount;

    public int[] findMode(TreeNode root) {
        modes = new ArrayList<>();
        currentVal = 0;
        currentCount = 0;
        maxCount = 0; 

        inorder(root);

        int [] res = new int[modes.size()];
        for (int i = 0; i < modes.size(); i ++){
            res[i] = modes.get(i); 
        }

        return res; 


    }

    private void inorder (TreeNode node){
        if (node == null) return; 

        inorder(node.left);

        // update the current count and current val; 
        if (node.val == currentVal){
            currentCount ++; 
        }else{
            currentVal = node.val;
            currentCount = 1;
        }

        // update the modes list:
        if (currentCount > maxCount){
            // clear the list:
            maxCount = currentCount;
            modes.clear();
            modes.add(currentVal); 
        }else if (currentCount == maxCount){
            modes.add(currentVal);
        }

        inorder(node.right);
    }
}
```

## Leetcode 236. 二叉树的最近公共祖先

#### 题目链接: [题目](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

#### 思路：
```Java
if (左子树有结果 && 右子树有结果) {
    // 当前节点就是LCA
    return 当前节点;
}
if (左子树有结果) {
    return 左子树的结果; // 向上传递
}
if (右子树有结果) {
    return 右子树的结果; // 向上传递
}
return null; // 两边都没有
```


```Java

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p, q);
    }

    private TreeNode dfs (TreeNode node, TreeNode p, TreeNode q){
        if (node == null) return null; 
        if (node == p || node == q) return node;

        TreeNode l_res = dfs(node.left, p, q);
        TreeNode r_res = dfs(node.right, p, q);

        // this means we found the node: 
        if (l_res != null && r_res != null){
            return node; 
        }

        if (l_res != null){
            return l_res;
        }

        if (r_res != null){
            return r_res;
        }

        return null; 

    }
}
```


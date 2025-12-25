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
这里就是用递归，每次我们会用中数去 create 一个 node，然后中数中数这个 node会有 left 和 right children，这时候我们再把两边切割的 Array 给左边和右边。这样我们一直递归下去，我们就做好了这个 tree。

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

通过反向中序遍历 + 累加和，从大到小更新节点值，利用 BST 有序性高效完成转换。

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



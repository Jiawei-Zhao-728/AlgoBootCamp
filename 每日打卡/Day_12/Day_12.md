# 代码随想录算法训练营第 12 天| 二叉树 part01

## 理论基础

需要了解：二叉树的种类、存储方式、遍历方式以及二叉树的定义

## 递归遍历（必须掌握）

二叉树的三种递归遍历掌握其规律后，其实很简单

### Leetcode 144. 二叉树的前序遍历

#### 题目链接： [题目](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

#### 思路：

前序遍历顺序：根 → 左 → 右；

递归三部曲：

确定递归函数参数和返回值
处理根节点
递归左子树
递归右子树

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        preorder(root, res);
        return res;



    }

    private void preorder (TreeNode node, List<Integer> result){
        if (node == null){
            return;
        }

        result.add(node.val);
        preorder(node.left, result);
        preorder(node.right, result);
    }
}
```

### Leetcode 145. 二叉树的后序遍历

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-postorder-traversal/)

#### 思路:

后序遍历顺序：左 → 右 → 根

递归三部曲：

1. 确定递归函数参数和返回值
2. 递归左子树
3. 递归右子树
4. 处理根节点

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        postorder(root, res);
        return res;

    }

    private void postorder (TreeNode node, List <Integer> result){
        if (node == null) return;

        postorder(node.left, result);
        postorder(node.right, result);
        result.add(node.val);
    }
}
```

### Leetcode 94. 二叉树的中序遍历

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

#### 思路：

中序遍历顺序：左 → 根 → 右

递归三部曲：

1. 确定递归函数参数和返回值
2. 递归左子树
3. 处理根节点
4. 递归右子树

时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，递归栈深度为树高

```Java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        inorder(root, res);
        return res;
    }

    private void inorder (TreeNode node, List <Integer> result){
        if (node == null) return;

        inorder(node.left, result);
        result.add(node.val);
        inorder(node.right, result);
    }
}
```

## 迭代遍历（基础不好的录友，迭代法可以放过）

### Leetcode 144. 二叉树的前序遍历（迭代法）

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

#### 思路:

前序遍历：根 → 左 → 右

用栈模拟递归：

1. 栈先 push 根节点
2. 每次 pop 一个节点，加入结果
3. 先 push 右子树，再 push 左子树（因为栈是后进先出）

```Java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        if (root == null) return res;

        Stack <TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()){
            TreeNode poped = stack.pop();
            res.add(poped.val);

            if(poped.right != null){
                stack.push(poped.right);
            }

            if (poped.left != null){
                stack.push(poped.left);
            }

        }

        return res;
    }
}
```

### Leetcode 94. 二叉树的中序遍历（迭代法）

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

#### 思路:

中序遍历：左 → 根 → 右

用指针 + 栈模拟：

1. 用指针 `cur` 从根节点开始
2. 一直往左走到底，把所有左节点 push 进栈
3. pop 栈顶（最左节点），加入结果
4. `cur = cur.right`，处理右子树
5. 重复步骤 2-4，直到 `cur == null` 且栈为空

关键：**先处理完所有左节点，再处理根，最后处理右**

```Java

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        Stack <TreeNode> stack = new Stack<>();
        TreeNode cur = root;

        while (cur != null || !stack.isEmpty()){
            while (cur != null){
                stack.push(cur);
                cur = cur.left;
            }

            // pop:
            cur = stack.pop();
            res.add(cur.val);


            cur = cur.right;

        }

        return res;

    }

}
```

### Leetcode 145. 二叉树的后序遍历（迭代法）

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-postorder-traversal/)

#### 思路:

后序遍历：左 → 右 → 根

**巧妙方法：基于前序遍历改 + reverse**

1. **前序遍历**：根 → 左 → 右（先 push 右，再 push 左）
2. **改一下顺序**：根 → 右 → 左（先 push 左，再 push 右）
3. **reverse 结果**：左 → 右 → 根 ✅

**为什么需要 reverse？**

- 后序遍历要求：左 → 右 → 根
- 但用栈直接实现很困难（需要标记是否访问过右子树）
- 所以先按 **根 → 右 → 左** 的顺序遍历（这个顺序用栈很好实现）
- 最后 **reverse** 就变成了 **左 → 右 → 根**

**记忆点**：后序 = 前序的"镜像"（左右顺序相反）+ reverse

```Java

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        if (root == null) return res;
        Stack <TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()){
            TreeNode poped = stack.pop();
            res.add(poped.val);

            if (poped.left != null){
                stack.push(poped.left);
            }

            if(poped.right != null){
                stack.push(poped.right);
            }


        }

        Collections.reverse(res);

        return res;
    }
}
```

## 层序遍历

看完本篇可以一口气刷十道题，试一试，层序遍历并不难，大家可以很快刷了十道题

### Leetcode 102. 二叉树的层序遍历

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

#### 思路:

这道题主要是用到了 BFS。唯一的技术难点就是在用 java 的时候 queue 要用 LinkedList 去开。

```Java

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List <List<Integer>> res = new ArrayList<>();
        if (root == null) return res;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()){
            int curSize = queue.size();
            List<Integer> curSub = new ArrayList<>();

            for (int i = 0; i < curSize; i++){
                TreeNode poped = queue.poll();
                curSub.add(poped.val);

                if (poped.left != null){
                    queue.offer(poped.left);
                }

                if (poped.right != null){
                    queue.offer(poped.right);
                }
            }

            res.add(curSub);
        }

        return res;



    }
}
```

### Leetcode 107. 二叉树的层次遍历 II

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)

#### 思路:

这道题就是在原有的基础上把 result reverse 了。

```Java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List <List<Integer>> res = new ArrayList<>();
        if (root == null) return res;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()){
            int curSize = queue.size();
            List<Integer> curSub = new ArrayList<>();

            for (int i = 0; i < curSize; i++){
                TreeNode poped = queue.poll();
                curSub.add(poped.val);

                if (poped.left != null){
                    queue.offer(poped.left);
                }

                if (poped.right != null){
                    queue.offer(poped.right);
                }
            }

            res.add(curSub);
        }

        Collections.reverse(res);

        return res;



    }
}
```

### Leetcode 199. 二叉树的右视图

#### 题目链接: [题目](https://leetcode.cn/problems/binary-tree-right-side-view/)

#### 思路:

和上面两题同样的思路利用 BFS，但是这次主要是只放每层最后一个 element。

```Java

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        if (root == null) return res;

        Queue <TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()){
            int level = queue.size();

            for (int i = 0; i < level; i ++) {
                TreeNode poped = queue.poll();

                if (i == level - 1){
                    res.add(poped.val);
                }

                if (poped.left != null){
                    queue.offer(poped.left);
                }
                if (poped.right != null){
                    queue.offer(poped.right);
                }
            }
        }

        return res;
    }
}
```

### Leetcode 637. 二叉树的层平均值

#### 题目链接: [题目](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

#### 思路:

思路一样，BFS，但是是计算每层的平均值。

```Java

class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List <Double> res = new ArrayList<>();
        if (root == null) return res;

        Queue <TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()){
            int cur_level = queue.size();
            double cur_sum = 0;

            for (int i = 0; i < cur_level; i++ ){
                TreeNode poped = queue.poll();
                cur_sum += poped.val;

                if(poped.left != null){
                    queue.offer(poped.left);
                }
                if(poped.right != null){
                    queue.offer(poped.right);
                }
            }

            res.add(cur_sum / cur_level);
        }

        return res;
    }

}
```

### Leetcode 429. N 叉树的层序遍历

#### 题目链接: [题目](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/)

#### 思路:

同样思路 BFS，但是用一个 loop 去 iterate children。

```Java
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List <List<Integer>> res = new ArrayList<>();
        if (root == null) return res;

        Queue <Node> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()){
            int curLevel = queue.size();
            List <Integer> currArray = new ArrayList<>();

            for (int i = 0; i < curLevel; i++){
                Node poped = queue.poll();
                currArray.add(poped.val);

                for (Node child : poped.children){
                    queue.offer(child);
                }
            }

            res.add(currArray);
        }

        return res;




    }
}
```

### Leetcode 515. 在每个树行中找最大值

#### 题目链接: [题目](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/)

#### 思路:

同样思路，找每层最大值。

```Java

class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        if (root == null) return res;

        Queue <TreeNode> queue = new LinkedList<>();
        queue.offer(root);


        while (!queue.isEmpty()){
            int level = queue.size();
            int maxVal = Integer.MIN_VALUE;

            for (int i = 0; i < level; i++){
                TreeNode poped = queue.poll();
                maxVal = Math.max(poped.val, maxVal);

                if (poped.left != null) {
                    queue.offer(poped.left);
                }

                if (poped.right != null) {
                    queue.offer(poped.right);
                }
            }

            res.add(maxVal);
        }

        return res;
    }
}
```

### Leetcode 116. 填充每个节点的下一个右侧节点指针

#### 题目链接: [题目](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

#### 思路:

同样思路 BFS。

```Java

class Solution {
    public Node connect(Node root) {
        if (root == null) return root;

        Queue <Node> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            int level = queue.size();

            for (int i = 0; i < level; i++){
                Node cur = queue.poll();

                if (i < level - 1){
                    cur.next = queue.peek();
                }

                if (cur.left != null) {
                    queue.add(cur.left);
                }

                if (cur.right != null){
                    queue.add(cur.right);
                }
            }
        }

        return root;
    }
}
```

### Leetcode 117. 填充每个节点的下一个右侧节点指针 II

#### 题目链接: [题目](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/)

#### 思路:

同样思路 BFS，比上面多一行，在每一行最后 null 一下

```Java

class Solution {
    public Node connect(Node root) {
        if (root == null) return root;

        Queue <Node> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            int level = queue.size();

            for (int i = 0; i < level; i++){
                Node cur = queue.poll();

                if (i < level - 1){
                    cur.next = queue.peek();
                }else{
                    cur.next = null;
                }

                if (cur.left != null) {
                    queue.add(cur.left);
                }

                if (cur.right != null){
                    queue.add(cur.right);
                }
            }
        }

        return root;
    }
}
```

### Leetcode 104. 二叉树的最大深度

#### 题目链接: [题目](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

#### 思路:

这道题，我们是需要知道每个节点的最大深度，是 max（左节点， 右节点）+ 1。

```Java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }

        int ldpeth = maxDepth(root.left);
        int rdepth = maxDepth(root.right);

        return 1 + Math.max(ldpeth, rdepth);
    }
}
```

### Leetcode 111. 二叉树的最小深度

#### 题目链接: [题目](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

#### 思路:

这里有点不一样，就是要考虑，当 l 或者 r subtree 有可能是 null，这时候本 node 的计算是 1 + 不为空的那个 node 深度。

```Java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int l = minDepth(root.left);
        int r = minDepth(root.right);

        if (root.left == null){
            return 1 + r;
        }

        if (root.right == null){
            return 1 + l;
        }

        return 1 + Math.min(l, r);
    }
}
```

## 总结

### 层序遍历核心模板（BFS）

```Java
Queue<TreeNode> queue = new LinkedList<>();
queue.offer(root);
while (!queue.isEmpty()){
    int level = queue.size();  // 关键：记录当前层大小
    for (int i = 0; i < level; i++){
        TreeNode cur = queue.poll();
        // 处理当前节点
        if (cur.left != null) queue.offer(cur.left);
        if (cur.right != null) queue.offer(cur.right);
    }
}
```

**关键点**：用 `level = queue.size()` 记录每层节点数，保证每层单独处理

### 层序遍历变形题

| 题目                 | 技巧                                                   |
| -------------------- | ------------------------------------------------------ |
| **102 层序遍历**     | 基础模板，每层存一个 List                              |
| **107 层次遍历 II**  | 基础模板 + `Collections.reverse(res)`                  |
| **199 右视图**       | 每层最后一个元素：`if (i == level - 1)`                |
| **637 层平均值**     | 每层求和后除以 `level`                                 |
| **429 N 叉树**       | 用 `for (Node child : node.children)` 遍历             |
| **515 每行最大值**   | 每层维护 `maxVal`，比较更新                            |
| **116/117 填充指针** | 同层节点：`if (i < level - 1) cur.next = queue.peek()` |

### 深度问题（递归）

- **104 最大深度**：`max(左深度, 右深度) + 1`
- **111 最小深度**：注意**单边为 null** 的情况，不能直接用 `min`，要判断：
  - 左 null → 返回 `1 + 右深度`
  - 右 null → 返回 `1 + 左深度`
  - 都不 null → 返回 `1 + min(左, 右)`

### 一句话总结

层序遍历 = **队列 + 记录每层大小**，掌握这个模板，所有层序变形题都能快速解决。深度问题用递归更简洁。

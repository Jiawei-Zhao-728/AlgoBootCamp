# 代码随想录算法训练营第 50 天 | 第十一章 图论 part01

## 图论入门：理论基础与 DFS/BFS

图论理论基础里很多内容一开始看不懂很正常（比如邻接矩阵、邻接表怎么用），先对各个概念有个印象就好，后面在刷题过程中每个知识点都会得到巩固。

## 图论理论基础

#### 说明：
看图论理论基础时，很多内容看不懂、看完也不知道邻接矩阵/邻接表怎么用，别着急。先对概念有个印象，刷题时会慢慢巩固。

#### 参考
- [图论理论基础](https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

---

## 深搜理论基础

#### 说明：
了解一下深搜的原理和过程。

#### 参考
- [深搜理论基础](https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E6%B7%B1%E6%90%9C%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

---

## 98. 所有可达路径

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0098)

#### 思路

比较基本，用 DFS


```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs (node, minVal, maxVal):
            if not node:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False

            return (dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal))

        return dfs(root, float('-inf'), float('inf'))
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0098.%E6%89%80%E6%9C%89%E5%8F%AF%E8%BE%BE%E8%B7%AF%E5%BE%84.html)

---

## 广搜理论基础

#### 说明：
了解广搜的原理与过程，与深搜对比理解。

#### 参考
- [广搜理论基础](https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E5%B9%BF%E6%90%9C%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

## 总结


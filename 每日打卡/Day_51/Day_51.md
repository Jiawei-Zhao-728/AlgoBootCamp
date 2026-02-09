# 代码随想录算法训练营第 51 天 | 第十一章 图论 part02

## 岛屿问题（深搜 / 广搜）

岛屿数量要掌握深搜、广搜的两种写法，并理解区别；注意广搜第一种写法易超时的原因，即使 AC 也建议看超时版本。

## 99. 岛屿数量

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0099)

#### 思路：

- **深搜**：注意深搜的**两种写法**，都要掌握，理解区别才能真正掌握 DFS。
- **广搜**：注意广搜的**两种写法**。第一种写法容易超时，即使通过了也建议仔细看超时版本、理解原因，否则下次可能过不了。


```Python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs (r, c):
            # check out of bound or land:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c) 
            dfs(r - 1, c)
            dfs(r, c + 1) 
            dfs(r, c - 1) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)
        

        return count

```

#### 参考
- [文章讲解（含深搜/广搜两种写法）](https://www.programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.html)

---

## 100. 岛屿的最大面积

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0100)

#### 思路：
基础题，上面 99 做完后这道应该很快。

差不多的 idea


```Python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs (r, c):
            # out of bound:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            # is water or visited:
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) )

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
            
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0100.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.html)

## 总结


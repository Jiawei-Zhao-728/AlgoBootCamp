# 代码随想录算法训练营第 52 天 | 第十一章 图论 part03

## 孤岛、水流、最大岛屿

101、102 是基础/变型，可先自己做；103、104 需要一点优化思路，想不出可直接看题解，优化方式会很有启发。

## 101. 孤岛的总面积

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0101)

#### 思路：
基础题目，可以自己尝试做一做。

没啥少活的


```Python
def close_island (grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs (r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        
        if grid[r][c] == 0:
            return


        grid[r][c] = 0

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for i in range(rows):
        for j in range(cols):
             if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                if grid[i][j] == 1:
                    dfs(i,j)
    
    res = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                res += 1

    return res


if __name__ == "__main__":
    n, m = map(int, input().split())

    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row) 

    res = close_island(grid)

    print(res)


```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0101.%E5%AD%A4%E5%B2%9B%E7%9A%84%E6%80%BB%E9%9D%A2%E7%A7%AF.html)

---

## 102. 沉没孤岛

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0102)

#### 思路：
和上一题差不多，尝试自己做做。


```Python
def sinkIsland(grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        # 越界或不是陆地
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return
        
        # 标记为2（安全陆地）
        grid[r][c] = 2
        
        # 四个方向DFS
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    # ===== 步骤1: 从边界DFS，标记安全陆地 =====
    
    # 上下边界
    for c in range(cols):
        if grid[0][c] == 1:          # 上边界
            dfs(0, c)
        if grid[rows - 1][c] == 1:   # 下边界
            dfs(rows - 1, c)
    
    # 左右边界
    for r in range(rows):
        if grid[r][0] == 1:          # 左边界
            dfs(r, 0)
        if grid[r][cols - 1] == 1:   # 右边界
            dfs(r, cols - 1)
    
    # ===== 步骤2: 处理结果 =====
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                grid[r][c] = 0   # 孤岛 → 沉没
            elif grid[r][c] == 2:
                grid[r][c] = 1   # 安全陆地 → 恢复

# ACM模式
if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    sinkIsland(grid)
    
    # 输出
    for row in grid:
        print(' '.join(map(str, row)))
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0102.%E6%B2%89%E6%B2%A1%E5%AD%A4%E5%B2%9B.html)

---

## 103. 水流问题

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0103)

#### 思路：
需要一点优化思路。建议先自己读题、想一个解题方法；有时间就自己写代码，没时间就直接看题解，优化方式会让你耳目一新。


```Python
def perform (heights):
    rows, cols = len(heights), len(heights[0])

    pacific = set()
    atlantic = set()

    def dfs (r, c, ocean):
        ocean.add((r,c))
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in  ocean and heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, ocean)


    for r in range(rows):
        dfs(r, 0, pacific)
    for c in range(cols):
        dfs(0, c, pacific)

    for r in range(rows):
        dfs(r, cols - 1, atlantic)
    for c in range(cols):
        dfs(rows - 1, c, atlantic)

    res = []
    for r, c in pacific &atlantic:
        res.append([r,c])

    return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    heights = []

    for _ in range(n):
        row = list(map(int, input().split()))
        heights.append(row) 

    res = perform(heights)
    for r, c in res:
        print(r, c)
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0103.%E6%B0%B4%E6%B5%81%E9%97%AE%E9%A2%98.html)

---

## 104. 建造最大岛屿

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0104)

#### 思路：
同样优化思路会让人耳目一新，自己想比较难想出来。


```Python
def perform (grid):
    rows, cols = len(grid), len(grid[0])
 
    def dfs(r, c, visited):
        # out of bound:
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited):
            return 0
 
        visited.add((r, c))
 
        area = 1
 
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            area += dfs(r + dr, c + dc, visited)
 
        return area
 
     
    max_area = 0
 
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                grid[i][j] = 1
                visited = set()
                area = dfs(i, j, visited)
                max_area = max(max_area, area)
                grid[i][j] = 0
 
     
    if max_area == 0:
        visited = set()
        max_area = dfs(0, 0, visited)
 
 
    return max_area
 
 
if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
 
    res = perform(grid)
 
 
    print(res)
/**************************************************************
    Problem: 1176
    User: odCYZ6tNsfMJQZ4DPlMvKcohDTJ0 [kamaCoder788554]
    Language: Python
    Result: 正确
    Time:1167 ms
    Memory:15952 kb
****************************************************************/
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0104.%E5%BB%BA%E9%80%A0%E6%9C%80%E5%A4%A7%E5%B2%9B%E5%B1%BF.html)

## 总结


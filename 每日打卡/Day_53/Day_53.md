# 代码随想录算法训练营第 53 天 | 第十一章 图论 part04

## 广搜应用、深搜细节、岛屿周长

广搜难不在广搜本身，而在如何应用；深搜要区分两种写法以及何时需要回溯；岛屿周长建议先独立做，避免惯性思维。

## 110. 字符串接龙

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0110)

#### 思路：
经过上面的练习，大家可能会感觉广搜不过如此、都刷出自信了。本题让大家初步感受一下：**广搜难不在广搜本身，而是如何应用广搜**。


```Python
from collections import deque

def solve(begin, end, word_list):
    word_list = set(word_list)
    word_list.add(end)

    queue = deque([(begin, 1)])
    visited = {begin}

    while queue:
        current, stops = queue.popleft()

        for i in range(len(current)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_string = current[:i] + c + current[i+1:]

                if new_string == end:
                    return stops + 1

                if new_string in word_list and new_string not in visited:
                    visited.add(new_string)
                    queue.append((new_string, stops + 1))

    return 0

if __name__ == "__main__":
    n = int(input().strip())          
    begin, end = input().strip().split()
    
    word_list = []
    for _ in range(n):                 
        word_list.append(input().strip())

    print(solve(begin, end, word_list))

```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0110.%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8E%A5%E9%BE%99.html)

---

## 105. 有向图的完全可达性

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0105)

#### 思路：
深搜有细节：同样是**深搜两种写法的区别**，以及**什么时候需要回溯操作**？


```Python

from collections import defaultdict

def solve(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = set()

    def dfs (node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(1)

    return 1 if len(visited) == n else 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    edges = []
    for _ in range(k):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    print(solve(n, edges))
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0105.%E6%9C%89%E5%90%91%E5%9B%BE%E7%9A%84%E5%AE%8C%E5%85%A8%E5%8F%AF%E8%BE%BE%E6%80%A7.html)

---

## 106. 岛屿的周长

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0106)

#### 思路：
简单题，避免大家惯性思维，建议**先独立做题**。


```Python
def islandPerimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # 是陆地
                # 检查四个方向
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    # 如果是水或越界，周长+1
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        perimeter += 1
    
    return perimeter

# ACM模式
if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    print(islandPerimeter(grid))
```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0106.%E5%B2%9B%E5%B1%BF%E7%9A%84%E5%91%A8%E9%95%BF.html)

## 总结


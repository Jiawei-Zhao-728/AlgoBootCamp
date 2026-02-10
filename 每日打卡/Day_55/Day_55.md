# 代码随想录算法训练营第 55 天 | 第十一章 图论 part05

## 并查集

并查集理论基础很重要：明确并查集解决什么问题、代码怎么写，对后面做并查集类题目很有帮助。107 是并查集裸题，学完理论可以直接刷过。

## 并查集理论基础

#### 说明：
并查集理论基础很重要。明确并查集**解决什么问题**、**代码如何写**，对后面做并查集类题目很有帮助。

#### 参考
- [并查集理论基础](https://www.programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E5%B9%B6%E6%9F%A5%E9%9B%86%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

---

## 107. 寻找存在的路径

#### 题目链接：[题目](https://kamacoder.com/problempage.php?id=0107)

#### 思路：
并查集裸题，学会理论基础后本题可以直接刷过。


```Python
from collections import defaultdict

def solve (n, edges, cource, destination):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    # dfs 遍历图，判断是否存在从 source 到 destination 的路径
    def dfs (node):
        if node == destination:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        
        return False

    return dfs(cource)

if __name__ == "__main__":
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    source, destination = map(int, input().split())

    result = solve(n, edges, source, destination)
    print (1 if result else 0)


```

#### 参考
- [文章讲解](https://www.programmercarl.com/kamacoder/0107.%E5%AF%BB%E6%89%BE%E5%AD%98%E5%9C%A8%E7%9A%84%E8%B7%AF%E5%BE%84.html)

## 总结


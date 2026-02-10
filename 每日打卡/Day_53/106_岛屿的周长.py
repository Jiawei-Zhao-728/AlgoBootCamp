"""
106. 岛屿的周长 (kamacoder ACM)
简单题，建议先独立做。
"""

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

    return 1 if len(visited) == n else -1

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    edges = []
    for _ in range(k):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    print(solve(n, edges))
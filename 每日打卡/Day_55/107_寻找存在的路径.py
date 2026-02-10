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


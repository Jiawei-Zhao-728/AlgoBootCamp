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
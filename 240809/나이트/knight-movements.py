from collections import deque


n = int(input().strip())
start_x, start_y, end_x, end_y = map(int, input().strip().split())

dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [-1, -2, -2, -1, 1, 2, 2, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs_knight(n, start, end):
    if start == end:
        return 0
    
    
    visited = [[False] * n for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not visited[nx][ny]:
                if (nx, ny) == (end[0], end[1]):
                    return dist + 1
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    
    return -1




start = (start_x - 1, start_y - 1)
end = (end_x - 1, end_y - 1)

print(bfs_knight(n, start, end))
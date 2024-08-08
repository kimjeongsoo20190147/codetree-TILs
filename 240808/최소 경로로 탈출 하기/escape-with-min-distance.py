from collections import deque

n,m = tuple(map(int, input().split()))
q = deque()
step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dxs, dys = [[1,0,-1,0], [0,1,0,-1]]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y) and not visited[new_x][new_y] and grid[new_x][new_y] != 0:
                push(new_x, new_y, step[x][y] + 1)


push(0,0,0)
bfs()
print(step[n-1][m-1])
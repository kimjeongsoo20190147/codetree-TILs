n = int(input())

x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    h_dir, dist = tuple(input().split())
    dist = int(dist)

    if h_dir == "E":
        x, y = x + dx[0]*dist, y + dy[0]*dist
    elif h_dir == "S":
        x, y = x + dx[1]*dist, y + dy[1]*dist
    elif h_dir == "W":
        x, y = x + dx[2]*dist, y + dy[2]*dist
    else:
        x, y = x + dx[3]*dist, y + dy[3]*dist

print(x,y)
h_dir = input()

x, y = 0, 0
dir_num = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for di in h_dir:
    if di == "L":
        dir_num = (dir_num - 1 + 4) % 4
    elif di == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x,y)
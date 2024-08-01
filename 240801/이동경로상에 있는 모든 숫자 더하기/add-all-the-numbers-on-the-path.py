n, t = map(int, input().split())
order = input()

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
dir_num = 2
dx, dy = [1,0,-1,0], [0,-1,0,1]

x, y = n//2, n//2
ans = arr[x][y]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

for di in order:
    if di == "L":
        dir_num = (dir_num - 1 + 4) % 4
    elif di == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]
        if in_range(x,y):
            ans += arr[x][y]
            #print(arr[x][y])
        else:
            x, y = x - dx[dir_num], y - dy[dir_num]

print(ans)
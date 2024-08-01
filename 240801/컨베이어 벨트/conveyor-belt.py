n, t = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 첫번째 줄 밀기
temp1 = grid[0][n-1]

for i in range(n-1, 0, -1):
    grid[0][i] = grid[0][i-1]

# 두번째 줄 밀기
temp2 = grid[1][n-1]

for i in range(n-1, 0, -1):
    grid[1][i] = grid[1][i-1]

# temp값들 앞에 넣기
grid[0][0] = temp2
grid[1][0] = temp1

for i in grid:
    for j in i:
        print(j, end=" ")
    print()
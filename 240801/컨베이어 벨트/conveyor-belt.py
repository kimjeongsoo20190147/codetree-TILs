n, t = map(int, input().split())
grid1 = list(map(int, input().split()))
grid2 = list(map(int, input().split()))


for _ in range(t):
    temp = grid1[n-1]
    for i in range(n-1, 0, -1):
        grid1[i] = grid1[i-1]
    grid1[0] = grid2[n-1]

    for i in range(n-1, 0, -1):
        grid2[i] = grid2[i-1]
    grid2[0] = temp



for elem in grid1:
    print(elem, end=" ")

print()

for elem in grid2:
    print(elem, end=" ")
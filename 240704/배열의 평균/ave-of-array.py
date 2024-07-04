arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    arr_sum = 0
    for j in range(4):
        arr_sum += arr[i][j]
    print(f"{arr_sum / 4:.1f}", end=" ")
print()


for i in range(4):
    arr_sum = 0
    for j in range(2):
        arr_sum += arr[j][i]
    print(f"{arr_sum / 2:.1f}", end=" ")
print()

arr_sum=0
for i in range(2):
    for j in range(4):
        arr_sum += arr[i][j]
print(f"{arr_sum / 8:.1f}", end=" ")
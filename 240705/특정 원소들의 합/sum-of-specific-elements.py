arr = [
    list(map(int, input().split()))
    for _ in range(4)
]


arr_sum=0

for i in range(4):
    for j in range(i+1):
        arr_sum += arr[i][j]
        

print(arr_sum)
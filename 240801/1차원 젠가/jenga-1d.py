n = int(input())
arr = [int(input()) for _ in range(n)]

a, b = map(int, input().split())
c, d = map(int, input().split())

temp1 = [0] * n
temp2 = [0] * n
end_of_temp_arr1 = 0
end_of_arr1 = n

end_of_arr2 = n
end_of_temp_arr2 = 0



for j in range(a-1, b):
    arr[j] = 0



for k in range(end_of_arr1):
    if arr[k] != 0:
        temp1[end_of_temp_arr1] = arr[k]
        end_of_temp_arr1 += 1

for i in range(end_of_temp_arr1):
    arr[i] = temp1[i]

end_of_arr1 = end_of_temp_arr1



for j in range(c-1, d):
    temp1[j] = 0

for k in range(end_of_arr2):
    if temp1[k] != 0:
        temp2[end_of_temp_arr2] = temp1[k]
        end_of_temp_arr2 += 1

for i in range(end_of_temp_arr2):
    temp1[i] = temp2[i]
end_of_arr2 = end_of_temp_arr2

# temp2가 최종

ans = 0

for elem in temp2:
    if elem != 0:
        ans += 1

print(ans)

for elem in temp2:
    if elem != 0:
        print(elem, end=" ")
    print()
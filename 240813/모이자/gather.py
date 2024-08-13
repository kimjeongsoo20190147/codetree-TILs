import sys

n = int(input())
arr = list(map(int, input().split()))

sum_dist = sys.maxsize
curr = 0

for i in range(n):
    for j in range(n):
        gap = abs(i-j)
        curr += arr[j] * gap
    sum_dist = min(curr, sum_dist)
    curr = 0

print(sum_dist)
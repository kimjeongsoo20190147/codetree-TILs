n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

#해당 영역 안에 코인 갯수 구하는 함수
def get_num_of_coin(row_s, row_e, col_s, col_e):
    num_of_coin = 0

    for col in range(col_s, col_e+1):
        for row in range(row_s, row_e+1):
            num_of_coin += grid[row][col]

    return num_of_coin


max_coin = 0

for row in range(n):
    for col in range(n):
        if col + 2 >= n or row + 2 >= n:
            continue

        num_of_coin = get_num_of_coin(row, row+2, col, col+2)
        max_coin = max(max_coin, num_of_coin)


print(max_coin)
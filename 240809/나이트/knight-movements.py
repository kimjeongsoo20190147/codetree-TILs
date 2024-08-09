n = int(input())

start_x, start_y, end_x, end_y = map(int, input().split())

visited = [[False] * n for _ in range(n)]
print(visited)

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n



def bfs(x,y):
    if x == y :
        return 0
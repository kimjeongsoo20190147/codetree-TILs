n = int(input())
ans = []
visited = [False]*(n+1)


def print_num():
    for elem in ans:
        print(elem, end=" ")
    print()



def choose_num(curr_num):
    if curr_num == n+1:
        print_num()
        return
    
    for i in range(1, n+1):
        if visited[i-1]:
            continue
        visited[i-1] = True
        ans.append(i)

        choose_num(curr_num+1)

        ans.pop()
        visited[i-1] = False


choose_num(1)
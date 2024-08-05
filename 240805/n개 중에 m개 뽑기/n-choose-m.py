n,m = tuple(map(int, input().split()))
ans = []

def print_num():
    for elem in ans:
        print(elem, end=" ")
    print()



def choose_num(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            print_num()
        return

    ans.append(curr_num)
    choose_num(curr_num+1, cnt+1)
    ans.pop()

    choose_num(curr_num+1, cnt)


choose_num(1,0)
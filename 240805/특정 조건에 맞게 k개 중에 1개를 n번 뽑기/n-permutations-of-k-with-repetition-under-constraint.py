k,n = tuple(map(int, input().split()))
ans = []

def print_num():
    for elem in ans:
        print(elem, end=" ")
    print()


def choose_num(cur_num):
    if cur_num == n:
        print_num()
        return
    
    for i in range(1, k+1):
        if cur_num >= 2 and i == ans[-1] and i == ans[-2]:
            continue
        else:
            ans.append(i)
            choose_num(cur_num+1)
            ans.pop()
    return


choose_num(0)
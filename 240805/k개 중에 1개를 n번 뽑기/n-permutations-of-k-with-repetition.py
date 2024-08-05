k, n = tuple(map(int, input().split()))
ans = []

def print_answer():
    for elem in ans:
        print(elem, end=" ")
    print()


def choose_num(curr_num):
    if curr_num  == n+1:
        print_answer()
        return
    
    for i in range(1, k+1):
        ans.append(i)
        choose_num(curr_num+1)
        ans.pop()

    return


choose_num(1)